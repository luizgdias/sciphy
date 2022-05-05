import os

def execute_sciphy_versions():
        with open('experiments/buffer2.txt', 'r') as file:
                for dataflow in file:
                        if('raxml' in dataflow) and ('clustalw' in dataflow):
                                os.system(dataflow)
                                #print(dataflow)

execute_sciphy_versions()
