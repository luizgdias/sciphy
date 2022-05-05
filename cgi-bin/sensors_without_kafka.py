import argparse
import psutil
import datetime
import json
import socket
import logging
from apscheduler.schedulers.blocking import BlockingScheduler
import apscheduler.events
import subprocess
from io import StringIO

# Globals
# TODO set through config file, if necessary
# These are the methods that are called to collect telemetry data. The fields returned by these calls define
# the telemetry schema. See the docs of psutil for possible methods: https://github.com/giampaolo/psutil
#
psutil_methods = [psutil.cpu_times,
                  psutil.virtual_memory,
                  psutil.swap_memory,
                  psutil.disk_io_counters]

# command for collecting GPU telemetry with NVIDIA
gpu_cmd = ["nvidia-smi --query-gpu=utilization.gpu,utilization.memory,memory.used,memory.total --format=csv"]


# The telemetry schema defines all the fields that are obligatorily collected. At each collect, one value of should be
# retrieved for each field in the schema. The script guarantees that if a value is not collected, it is set as None.
telemetry_schema = []

# The telemetry buffer dictionary holds all the collected measurements. It is reset upon dispatch.
telemetry_buffer = {}

# The producer, scheduler
producer = None
sched = None


def set_telemety_schema():
    ''' Builds a list of fields based on the return values of the methods in psutil_methods.
    :return: A list of strings, where each string defines a field for telemetry data collection
    '''
    global psutil_methods, telemetry_schema
    for method in psutil_methods:
        named_tuple = method()
        name = type(named_tuple).__name__
        fields = named_tuple._fields
        for field in fields:
            telemetry_schema.append(name + '_' + field)


    if args.sensoring_gpu:
        p = subprocess.Popen(gpu_cmd, shell=True, stdout=subprocess.PIPE)
        lines = []
        for line in iter(p.stdout.readline, ''):
            lines.append([s.strip().replace(' ', '').replace('%', '').replace('[]', '') for s in line.split(',')])

        for field in lines[0]:
            telemetry_schema.append('gpu.' + field)

    print(telemetry_schema)


def reset_telemetry_buffer():
    ''' Resets the telemetry buffer as a dict of the schema where each field has an empty list as value. Also adds
    a 'timestamp' key to hold the timestamps of each telemetry data collections. '''
    global telemetry_buffer, telemetry_schema
    telemetry_buffer = {k: list() for k in telemetry_schema}
    telemetry_buffer['timestamp'] = []


def add_telemetry(telemetry_tuple, telemetry_dict):
    ''' Given a named tuple a(x=v1,y=v2,...,z=vn) and a dict with keys 'a_x','a_y',...,'a_z', maps 'a_x' to v1, 'a_y' to
    v2, ..., 'a_z' to vn. If any of the keys 'a_x','a_y',...,'a_z' do not exist on the telemetry schema, the corresponding
    telemetry measurment is discarded.
    :param telemetry_tuple: named tuple, as returned by the methods in psutil_methods
    :param telemetry_dict: a dict, as built from the telemetry schema
    :return:
    '''
    for k, v in telemetry_tuple._asdict().items():
        key_name = type(telemetry_tuple).__name__ + '_' + k
        if key_name not in telemetry_dict.keys():
            logging.warning("Telemetry currently collected contains key not in the schema: " + key_name + " " + str(v))
        else:
            telemetry_dict[key_name] = v

def attempt_convertion(v):
  try:
    return eval(v)
  except SyntaxError:
    return v

def add_gpu_telemetry(telemetry_dict):
    """
    Captures the GPU telemetry using nvidia-smi tool,
    :param telemetry_dict: The telemetry containing telemetry data.
    :return:
    """
    try:
        p = subprocess.Popen(gpu_cmd, shell=True, stdout=subprocess.PIPE)

        lines = []
        for line in iter(p.stdout.readline, ''):
            lines.append([s.strip().replace(' ', '').replace('%', '').replace('[]', '') for s in line.split(',')])

        # turn the two lines into a dict like first_line_i -> second_line_i
        gpu_telemetry = dict(zip(['gpu.' + s for s in lines[0]], [attempt_convertion(s) for s in lines[1]]))
        #print gpu_telemetry

        # update the "global" telemetry
        telemetry_dict.update(gpu_telemetry)

    except subprocess.CalledProcessError as e:
        logging.error(str(e))


def collect_and_dispatch():
    global telemetry_buffer
    collect()
    if len(telemetry_buffer['timestamp']) == args.dispatch_calls:
        dispatch()
        reset_telemetry_buffer()


def collect():
    ''' Take current telemetry data and bufferize it in the telemetry buffer. Guarantees that one value
    is collected for each field in the telemetry schema. '''
    global psutil_methods, telemetry_buffer, telemetry_schema
    logging.info('Collect event at ' + str(datetime.datetime.now()))
    current_telemetry = {k: None for k in telemetry_schema}
    for method in psutil_methods:
        add_telemetry(method(), current_telemetry)

    if args.sensoring_gpu:
        add_gpu_telemetry(current_telemetry)

    # Verify whether all fields in the schema were collected, fills non-collected fields with none
    missing_fields = get_missing_schema_fields(current_telemetry)
    for field in missing_fields:
        current_telemetry[field] = None

    # Add all current_telemetry measumerements to the telemetry buffer
    for k, v in current_telemetry.items():
        telemetry_buffer[k].append(v)
    telemetry_buffer['timestamp'].append(str(datetime.datetime.now()))


def dispatch():
    ''' Sends the buffered telemetry to file. Resets and clears
    the telemetry buffer. '''
    global telemetry_buffer
    logging.info('Dispatch event at ' + str(datetime.datetime.now()))
    if check_buffer_consistency():
        producer.write(json.dumps(telemetry_buffer) + '\n')
        producer.flush()


def get_missing_schema_fields(telemetry_dict):
    global telemetry_schema
    missing_fields = []
    for field in telemetry_schema:
        if field not in telemetry_dict:
            missing_fields.append(field)
    return missing_fields


def check_buffer_consistency():
    global telemetry_buffer

    # Making sure all fields are in the buffer
    missing_fields = get_missing_schema_fields(telemetry_buffer)
    if missing_fields:
        logging.info("Telemetry buffer missing fields from the schema.")
        return False

    # Make sure all keys in the buffer map to lists of same values
    lens = [len(v) for v in telemetry_buffer.values()]
    if len(set(lens)) > 1:
        logging.info("Telemetry buffer contains missing collected data in some fields")
        return False
    return True


def timeout():
    ''' Stops the scheduler, shutting it down after removing all jobs. '''
    global sched
    logging.info('Timeout event at ' + str(datetime.datetime.now()))
    sched.remove_job('job')


def build_and_start_scheduler():
    ''' Setup and run!'''
    global sched, job_collect, job_dispatch

    # TODO a smarter scheduling, if necessary
    sched = BlockingScheduler()
    sched.add_job(collect_and_dispatch, 'interval', seconds=args.collect_interval, max_instances=1, id='job')
    # if args.timeout:
    #    now = datetime.datetime.now()
    #    then = now + datetime.timedelta(seconds=args.timeout)
    #    sched.add_job(timeout, 'date', run_date=then)
    try:
        sched.start()
    except (KeyboardInterrupt, SystemExit):
        print("Scheduler terminated by user or external process.")
        logging.info("Scheduler terminated by user or external process.")
        sched.shutdown()
        dispatch()
        producer.close()
        logging.shutdown()


if __name__ == '__main__':
    ''' Collects and bufferizes sensor telemetry data in regular intervals. Dispatches KafkaProducer messages containing
    these data to the Kafka topic given as target, in regular intervals given by dispatch_interval. If dispatch_interval
    is zero, dipatches only when the script terminates.

    The script terminates after --timeout seconds or when terminated by the user. When terminating, dispatches whatever
    telemetry data are buffered.'''
    parser = argparse.ArgumentParser()
    # Required
    # parser.add_argument(dest='target', help='Kafka topic to dispatch the sensor data.')
    parser.add_argument(dest='collect_interval', type=int, help='Interval (in seconds) to collect sensor data.')
    parser.add_argument(dest='dispatch_calls', type=int,
                        help='Required number of observations to dispatch sensor data, or -1 to dispatch only when the the script terminates.')
    # Optional
    parser.add_argument('-f', '--filename', dest='filename', help='File to write telemetry data',
                        default=socket.gethostname() + '.telemetry')
    parser.add_argument('--log', dest='log_fn', nargs='?', default='sensors.log')
    parser.add_argument('-d', '--debug', help="Print lots of debugging statements", action="store_const",
                        dest="log_level", const=logging.DEBUG, default=logging.WARNING)
    parser.add_argument('-v', '--verbose', help="Be verbose", action="store_const", dest="log_level",
                        const=logging.INFO)
    parser.add_argument('-g', '--gpu', help='flag to ask sensors.py to collect telemtry from GPU using nvidia_smi',
                        action="store_true", dest="sensoring_gpu", default=False)

    args = parser.parse_args()

    # Setup
    logging.basicConfig(filename=args.log_fn, level=args.log_level)
    producer = open("telemetria.txt", 'w')

    set_telemety_schema()
    reset_telemetry_buffer()
    build_and_start_scheduler()
