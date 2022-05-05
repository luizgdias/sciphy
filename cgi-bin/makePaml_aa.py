#! /usr/bin/env python

# TITULO            : Make Paml
# AUTOR             : Kary Soriano
# DATA              : 15/01/2008
# DIFICULDADE       : 1
# ==============================================================================
# Objetivo do script: Executado do profile_phylogeny_aa.py
#                     Executa Paml. ###ver que vai fazer e como implementar
# (VIVAX)           : python ...
# ==============================================================================
# Data da ultima alteracao do script: 12/02/2008
#                                   : //2008
# ==============================================================================
#-------------------------------------------------------------------------------
# declarando os modulos a usar 
#-------------------------------------------------------------------------------
import sys, os, re
import shutil as sh
#-------------------------------------------------------------------------------
###dirin = sys.argv[1]								# print "O nome do caminho e arquivo de entrada e: " + dirin_do_ficheiro 
###arg = sys.argv[1:]						  		# print "Os argumentos passados sao: " + str(dirin_arg_pas)

###def paramCleanPaml(dirin, mg):
###  # Abrindo o paml para leitura
###  print "Opening the existing " + mg + " for read"
###  path_mg = os.path.join(dirin, mg)
###  os.chmod(path_mg, 0755)  # Assume it's a file
###  # Lendo o arquivo paml0.out para editar e obter parametros AIC1, AIC2 ou BIC
###  text_mg = open(path_mg).read()
###  # Extraindo informacao de paml0.out 
###  mg_parameter = text_mg.split("\n\n****Akaike Information Criterion 1 (AIC1)****\n\n")
###  mg_info = mg_parameter[1].split(":")                                          # mg_info[1] = modelo e parametros limpos
###  #parametro_filogenia = mg_info[1].split("+")
###  parametro_filogenia = re.split(r'\+|\n', mg_info[1])                          # os parametros de Modelos Evolutivos sao MODEL+I+G+F (estes tres ultimos sao os parametros e nao tem ordem definida)
###  parametro_filogenia_clean = parametro_filogenia[0].replace(" ", "")           # Limpando de espacos em branco
###  #print "The evolutionary model found is: " + parametro_filogenia_clean
###  return parametro_filogenia_clean

###def paramMoveFilesPaml(dirin, path_mafft):
###  # Movendo ".out", "_phymlBoot.sh", "_phyml.sh", "_puzzleBoot.sh", "_treePuzzle.sh"
###  dirin_out_final = path_mafft.split("/")
###  dirin_out_final.pop()
###  out_final = "/".join(dirin_out_final)
###  print "Moving paml0.out and *.sh files " + "from " + dirin + " to " + out_final
###  for file_move in os.listdir(dirin):
###    if file_move.endswith('.out'):
###      sh.move(file_move, out_final)						
###    if file_move.endswith('.sh'):
###      sh.move(file_move, out_final)						
###    
def ParamModulePaml(dirin, param_model_evol):
  found = False
  for mg in os.listdir(dirin):
# 1.- Constatando se existe paml0.out
    if re.search ('.out$', mg):
      found  = True
      ###print "There is a " + mg + " file"
    #Chamando def paramCleanPaml
      #paramCleanPaml(dirin, mg)
      #print "TESTE The evolutionary model found is: " + paramCleanPaml(dirin, mg)
###      return paramCleanPaml(dirin, mg)
#### 2.- Executando o paml do shell
###  if found is False:
###    print "Building the Paml file using Mafft"
###    cmd_mg = "java -jar /usr/local/paml/paml.jar " + path_mafft + " 6 " 
###    handle_mg = os.popen(cmd_mg, 'r', 1)
###    for line_mg in handle_mg:
###      print line_mg,
###    handle_mg.close()
#### 3.- Trabalhando com o diretorio onde e criado o paml0.out.- 
###    dirin = currentdirectory = os.getcwd( )
###    for mg in os.listdir(dirin):
#### 2.- Criando o novo paml0.out
###      if re.search ('paml0.out$', mg):
###        found  = True
###        print "Was created " + mg + " file " + "in " + dirin
###        #Chamando def paramCleanPaml
###        #paramCleanPaml(dirin, mg)  
###        return paramCleanPaml(dirin, mg)  
###        #Chamando def paramMoveFilesPaml
###        paramMoveFilesPaml(dirin, path_mafft)
