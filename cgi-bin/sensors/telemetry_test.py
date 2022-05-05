# -*- coding: utf-8 -*-
import psutil
#from pathlib import Path
import os, sys
import psutil
import time
os.popen('python -V')



cmd_telemetria = 'python sensors_without_kafka.py 1 1'
os.popen('python -V')

os.popen(cmd_telemetria)
time.sleep(15)
os.popen('ps axf | grep sensors_without_kafka.py | grep -v grep | awk \'{print \"kill -9 \" $1}\' | sh')


os.popen('python -V')


# class Telemetria:
#     def __init__(self, intervalo=0, segundos=0, date=0, time=0):
#         date_time   = "date +\"%T\""
#         date        = "date +\"%d-%m-%y\""

#         #---- Info padrão da telemetria
#         self.intervalo = intervalo
#         self.segundos = segundos
#         self.date   = os.popen(date).read()
#         self.time   = os.popen(date_time).read()

#         #---- Info sobre métricas específicas
#         self.qtd_cpu        = 0
#         self.disco_livre    = 0
#         self.uso_disco      = 0
#         self.porcentagem_uso_cpu_user          = 0
#         self.porcentagem_uso_cpu_system        = 0
#         self.porcentagem_uso_memoria    = 0
#         self.network_rec    = 0
#         self.network_sent   = 0



# #--------------------------------------------------------------------------------
#     def capturaTelemetria(self):

#         disco   = psutil.disk_usage('/')
#         memoria = psutil.virtual_memory()
#         network = psutil.net_io_counters()




#         #----info sobre cpu
#         #psutil.cpu_times_percent(interval=None, percpu=False)-> Same as cpu_percent() but provides utilization percentages for each specific CPU time as
#         #is returned by psutil.cpu_times(percpu=True). interval and percpu arguments have the same meaning as in cpu_percent().
#         #On Linux “guest” and “guest_nice” percentages are not accounted in “user” and “user_nice” percentages.
#         self.qtd_cpu    = os.popen("grep -c ^processor /proc/cpuinfo").read()
#         self.porcentagem_uso_cpu = psutil.cpu_percent()
#         #----

#         #----info sobre disco? sdiskusage(total=115643510784, used=31927046144, free=77797990400, percent=29.1)
#         self.porcentagem_uso_disco = disco.used
#         self.disco_livre = disco.free
#         #----

#         #----info sobre memória: svmem(total=4012335104, available=860672000, percent=78.5, used=2229579776, free=262262784, active=2368192512,
#         #inactive=1025183744, buffers=93216768, cached=1427275776, shared=672907264, slab=183123968)
#         self.porcentagem_uso_memoria = memoria.percent
#         self.memoria_virtual = psutil.virtual_memory()

#         #----info sobre network
#         self.network_rec = network.bytes_recv
#         self.network_sent = network.bytes_sent

#         #print("data: ", self.date)
#         #print("hora: ", self.time)
#         #print("qtd cpu: "+ self.qtd_cpu)
#         #print("% uso cpu: ", self.porcentagem_uso_cpu)
#         #print("% uso disco: ", self.porcentagem_uso_disco)
#         #print("% memória virtual: ", self.porcentagem_uso_memoria)
#         #print("Espaço disco livre: ", self.disco_livre)
#         #print("Bytes recebidos: ", self.network_rec)
#         #print("Bytes enviados: ", self.network_sent)
#         #print(network)


# #--------------------------------------------------------------------------------
#             #**legenda sobre os resultados listados apos a ediscoecução do comando: sar X Y:

#         	#$1: %system: Porcentagem de utilização da CPU que ocorreu durante a execução no nível do sistema (kernel).
#         	#$2: %iowait: Porcentagem de tempo em que a CPU ou as CPUs ficaram inativas durante.
#         	#o qual o sistema tinha uma solicitação de E / S de disco pendente.
#         	#$3: %user: Porcentagem de utilização da CPU que ocorreu durante a execução no nível do usuário>
#         	#$4: %nice: Porcentagem de utilização da CPU que ocorreu durante a execução no nível do usuário com boa prioridade.
#         	#$5 %system: Porcentagem de utilização da CPU que ocorreu durante a execução no nível do sistema (kernel).
#         	#$6: %iowait: Porcentagem de tempo em que a CPU ou as CPUs ficaram inativas durante.
#         	#o qual o sistema tinha uma solicitação de E / S de disco pendente.
#         	#$7: %steal: Porcentagem de tempo gasto em espera involuntária pela CPU virtual ou CPUs.
#         	#$8: %idle: Porcentagem de tempo em que a CPU ou as CPUs estavam ociosas e o sistema não tinha uma solicitação
#         	#de E / S de disco pendente.

#     def telemetry_cpu_usage(self):
#         #print("%user-> cpu utilizada nível de usuário")
#         #print("%system-> cpu utilizada nível de sistema (kernel)")
#         print("** Telemetry Data **")
#         print("Loading cpu telemetry info...")
#         #arg = 'sar ' + str(self.intervalo) +' '+ str(self.segundos) + "| awk {\'print \" \", $1, $3, $5\'}"
#         arg = 'sar ' + str(self.intervalo) +' '+ str(self.segundos) + " | awk {\'print \" \",$3\'} |tail -1 "
#         self.porcentagem_uso_cpu_user = os.popen(arg).read()
#         print("Percentual uso de cpu %user: " , self.porcentagem_uso_cpu_user)

#         arg = 'sar ' + str(self.intervalo) +' '+ str(self.segundos) + " | awk {\'print \" \",$5\'} | tail -1 "
#         self.porcentagem_uso_cpu_system = os.popen(arg).read()
#         print("Percentual uso de cpu %system: " , self.porcentagem_uso_cpu_system)

#         #popen é necessário para salvar os valores do os em variáveis/objetos
#         self.qtd_cpu    = os.popen("grep -c ^processor /proc/cpuinfo").read()
#         print("QTD CPUS: "+ str(self.qtd_cpu))




# #--------------------------------------------------------------------------------
#     #**legenda sobre os resultados listados apos a execução do comando: sar -r X Y:

# 	#$1: kbmemfree: Quantidade de memória livre disponível em kilobytes.
# 	#$2: kbavail:
# 	#$3: kbmemused: Quantidade de memória usada em kilobytes. Isso não leva em conta a memória usada pelo próprio kernel.
# 	#$4: %memused: Quantidade de memoria utilizada.
# 	#$5: %kbbuffers: Quantidade de memória usada como buffers pelo kernel em kilobytes.
# 	#$6: %kbcached: Quantidade de memória usada para armazenar dados em cache pelo kernel em kilobytes.
# 	#$7: kbcommit: Quantidade de memória em kilobytes necessários para a carga de trabalho atual.
# 	# Essa é uma estimativa de quanto de RAM / troca é necessária para garantir que nunca haja falta de memória.
# 	#$8: kbactive:
# 	#$9: kbinact:
# 	#$10: kbdirty




    
#     def telemetry_memory_usage(self):
#         #print("kbmemused-> memória utilizada\n")
#         #arg = 'sar -r ' + str(self.intervalo) +' '+ str(self.segundos) + " | awk {\'print \" \", $1, $5\'}"
#         print("** Telemetry Data **")
#         print("Loading memory telemetry info...")
#         arg = 'sar -r ' + str(self.intervalo) +' '+ str(self.segundos) + " | awk {\'print \" \", $5\'}  | tail -1"
#         self.porcentagem_uso_memoria = os.popen(arg).read()
#         print("Intervalo: "         , self.intervalo)
#         print("Segundos: "          , self.segundos)
#         print("Percentual uso de memoria: " , self.porcentagem_uso_memoria)



# #--------------------------------------------------------------------------------
#     def telemetry_disk_usage(self):
#         arg = 'sar -n DEV 1 10'
#         self.porcentagem_uso_disco = os.popen(arg).read()
#         print("disco: ", self.porcentagem_uso_disco)

