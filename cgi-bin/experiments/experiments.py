import os


def list_sequence():
        os.system('rm sequence_list.txt')
        os.system('touch sequence_list.txt ')
        sequences       = open('sequence_list.txt', "a")
        for root, dirs, files in os.walk("../inputTestGc", topdown=False):
                for name in files:
                        #sequences.write("python2 arpa.py -t aa -o out -a mafft -p raxml -c total "+name+"\n")
                        sequences.write(name+"\n")
                        
                sequences.close()


def create_experiments():
        os.system('rm buffer.txt')
        os.system('touch buffer.txt')
        buffer_dataflows = open('buffer.txt', 'a')
        cont = 0
        with open('ontology/derivations/sciphyversions.txt', 'r') as file:
                for dataflow in file:
                        with open('sequence_list.txt', "r") as sequences:
                                        for name in sequences:
                                                x = (str(dataflow.strip('\n') +" inputTestGc/"+ (name.strip('\n')))+"\n")
                                                buffer_dataflows.write(x)
                                                cont = cont +1

def replace_ontology_dataflows_to_sciphy_prompt():
        os.system('rm buffer2.txt')
        os.system('touch buffer2.txt')
        buffer_dataflows = open('buffer2.txt', 'a')
        cont = 0
        with open('buffer.txt', 'r') as file:
                for dataflow in file:
                        #print(dataflow)
                        #python2 arpa.py -t aa -o out -a mafft -p raxml -c total ORTHOMCL256 
                        dataflow = dataflow.replace("clear:EDAM_termos.RemovePipe; -> ", " ")

                        dataflow = dataflow.replace("alignment:EDAM_termos.Tcoffee; -> ", 'python2 arpa.py -t aa -o out -a tcoffee')
                        dataflow = dataflow.replace("alignment:EDAM_termos.Probcons; -> ", 'python2 arpa.py -t aa -o out -a probcons')
                        dataflow = dataflow.replace("alignment:EDAM_termos.Muscle; -> ", 'python2 arpa.py -t aa -o out -a muscle')
                        dataflow = dataflow.replace("alignment:EDAM_termos.Mafft; -> ", 'python2 arpa.py -t aa -o out -a mafft')
                        dataflow = dataflow.replace("alignment:EDAM_termos.ClustalW; -> ", 'python2 arpa.py -t aa -o out -a clustalw')

                        dataflow = dataflow.replace("converter:EDAM_termos.ReadSeq; -> ", ' ')
                        dataflow = dataflow.replace("modelgenerator:EDAM_termos.ModelGenerator; -> ", ' ')

                        dataflow = dataflow.replace("treegenerator:EDAM_termos.Raxml ", '-p raxml -c total ')
                        dataflow = dataflow.replace("treegenerator:EDAM_termos.MrBayes", '-p mrbayes -c total ')
                        dataflow = dataflow.replace("treegenerator:EDAM_termos.Garli", '-p garli -c total ')
                        dataflow = dataflow.replace("treegenerator:EDAM_termos.PhyML", '-p phyml -c total ')

                        buffer_dataflows.write(dataflow)

# def execute_sciphy_versions():
#         with open('buffer2.txt', 'r') as file:
#                 for dataflow in file:
#                         if('raxml' in dataflow):
#                                 #print(dataflow)
#                                 os.system(dataflow)
                                

list_sequence()
create_experiments()
replace_ontology_dataflows_to_sciphy_prompt()
#execute_sciphy_versions()
