import requests
import os
from .ProvenanceObject import ProvenanceObject
from .dependency import Dependency
from .task_status import TaskStatus
from .dataset import DataSet
from .performance import Performance
from .telemetry import Telemetry
from .telemetry_cpu import TelemetryCPU
from .telemetry_disk import TelemetryDisk
from .telemetry_memory import TelemetryMemory
from .telemetry_network import TelemetryNetwork
from .epoch import Epoch
from datetime import datetime

dfa_url = os.environ.get('DFA_URL',"http://localhost:22000/")


class Task(ProvenanceObject):
    """
    This class defines a dataflow task.

    Attributes:
        - id (:obj:`str`): Task Id.
        - dataflow_tag (:obj:`str`): Dataflow tag.
        - transformation_tag (:obj:`str`): Transformation tag.
        - sub_id (:obj:`str`, optional): Task Sub Id.
        - dependency (:obj:`Task`): Task which the object has a dependency.
        - workspace (:obj:`str`, optional): Task workspace.
        - resource (:obj:`str`, optional): Task resource.
        - output (:obj:`str`, optional): Task output.
        - error (:obj:`str`, optional): Task error.
    """#
    #o parametro id foi retirado do construtor para possibilitar execução de varios experimentos alterando apenas o nome do dataflow. (o que não era possivel com esse atributo)
    #caso seja necessário, descomente a linha 50 e insira novamente o atributo id após o self na linha 36
    def __init__(self, dataflow_tag, transformation_tag,
                 sub_id="", dependency=None, workspace="", resource="",
                 output="", error=""):
        ProvenanceObject.__init__(self, "{0}_{1}".format(dataflow_tag,
                                                         transformation_tag))
        self._workspace = workspace
        self._resource = resource
        self._dependency = ""
        self._output = output
        self._error = error
        self._sets = []
        self._status = TaskStatus.READY.value
        self._dataflow = dataflow_tag.lower()
        self._transformation = transformation_tag.lower()
        #self._id = str(id)
        self._sub_id = sub_id
        self._performances = []
        self._epoch = []
        self._telemetries = ""
        self._cpu = ""
        self._disk = ""
        self._memory = ""
        self._network = ""
        self.dfa_url = dfa_url
        self.start_time = None
        self.end_time = None
        if isinstance(dependency, Task):
            dependency = Dependency([dependency._tag], [dependency._id])
            self._dependency = dependency.get_specification()

    def add_dependency(self, dependency):
        """ Add a dependency to the Task.

        Args:
            - dependency (:obj:`Dependency`): A :obj:`Dependency` object.
        """

        assert isinstance(dependency, Dependency), \
            "The dependency must be valid."
            print ("etc")
        self._dependency = dependency.get_specification()
        #self.save()

    def set_datasets(self, datasets):
        """ Set the Task DataSets.

        Args:
            - dataset (:obj:`list`): A :obj:`list` containing :obj:`DataSet` objects.
        """
        assert isinstance(datasets, list), \
            "The parameter must be a list."
        for dataset in datasets:
            self.add_dataset(dataset)
        #self.save()

    def add_dataset(self, dataset):
        """ Add a dataset to the Task.

        Args:
            - dataset (:obj:`DataSet`): A :obj:`DataSet` object.
        """
        assert isinstance(dataset, DataSet), "The dataset must be valid."
        self._sets.append(dataset.get_specification())
        #self.save()

    def add_epoch(self, epoch):
        assert isinstance(epoch, Epoch), "The epoch must be valid."
        self._epoch.append(epoch.get_specification())
        #self.save()  

    def add_telemetry(self, telemetry):
        assert isinstance(telemetry, Telemetry), "The telemetry must be valid."
        self._telemetries = [telemetry.get_specification()]
        #self.save()        

    def add_telemetry_cpu(self, telemetry_cpu):
        assert isinstance(telemetry_cpu, TelemetryCPU), "The telemetry cpu must be valid."
        self._cpu = [telemetry_cpu.get_specification()]
        #self.save() 

    def add_telemetry_disk(self, telemetry_disk):
        assert isinstance(telemetry_disk, TelemetryDisk), "The telemetry disk must be valid."
        self._disk = [telemetry_disk.get_specification()]
        #self.save()    

    def add_telemetry_memory(self, telemetry_memory):
        assert isinstance(telemetry_memory, TelemetryMemory), "The telemetry memory must be valid."
        self._memory = [telemetry_memory.get_specification()]
        #self.save() 

    def add_telemetry_network(self, telemetry_network):
        assert isinstance(telemetry_network, TelemetryNetwork), "The telemetry network must be valid."
        self._network = [telemetry_network.get_specification()]
        #self.save()                       

    def set_status(self, status):
        """ Change the Task Status.

        Args:
            - status (:obj:`TaskStatus`): A :obj:`TaskStatus` object.
        """
        assert isinstance(status, TaskStatus), \
            "The task status must be valid."
        self._status = status.value

    def begin(self):
        """ Send a post request to the Dataflow Analyzer API to store the Task.
        """        
        self.set_status(TaskStatus.RUNNING)
        self.start_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        self.save()
        self._sets = []

    def end(self):
        """ Send a post request to the Dataflow Analyzer API to store the Task.
        """
        self.set_status(TaskStatus.FINISHED)
        self.end_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        performance = Performance(self.start_time, self.end_time)
        self._performances.append(performance.get_specification())
        # telemetry = Telemetry("1", "2", "4")
        # self._telemetries.append(telemetry.get_specification())
        self.save()
        self._sets = []

    def save(self):
        """ Send a post request to the Dataflow Analyzer API to store the Task.
        """
        url = dfa_url + '/pde/task/json'
        message = self.get_specification()
        print(message)
        r = requests.post(url, json=message)
        print(r.status_code)