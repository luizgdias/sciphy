#! /usr/bin/env python

# TITULO            : Make Modelgenerator
# AUTOR             : Kary Soriano
# DATA              : 15/01/2008
# DIFICULDADE       : 1
# ==============================================================================
# Objetivo do script: Executado do arpa.py
#                     Executa Modelgenerator. Da modelo evolutivo (AIC1 [usada], AIC2, BIC) e
#                     Saida de parametros phymlBoot.sh, phyml.sh, puzzleBoot.sh, treePuzzle.sh
# ==============================================================================
# Data da ultima alteracao do script: 30/01/2008
#                                   : 15/01/2008
# ==============================================================================
#-------------------------------------------------------------------------------
# declarando os modulos a usar 
#-------------------------------------------------------------------------------
import sys, os, re
import shutil as sh
#-------------------------------------------------------------------------------
def paramCleanModelgenerator(dirincurrent, mg):
  # Abrindo o modelgenerator para leitura
  print "\tOpening the existing " + mg + " for read"
  path_mg = os.path.join(dirincurrent, mg)
  print mg
  print path_mg
  os.chmod(path_mg, 0755)  # Assume it's a file
  # Lendo o arquivo modelgenerator0.out para editar e obter parametros AIC1, AIC2 ou BIC
  text_mg = open(path_mg).read()
  # Extraindo informacao de modelgenerator0.out 
  mg_parameter = text_mg.split("\n\n****Akaike Information Criterion 1 (AIC1)****\n\n")
  mg_info = mg_parameter[1].split(":")                                          # mg_info[1] = modelo e parametros limpos
  parametro_filogenia = mg_info[1].split("\n")                          # os parametros de Modelos Evolutivos sao MODEL+I+G+F (estes tres ultimos sao os parametros e nao tem ordem definida)
  parametro_filogenia_clean = parametro_filogenia[0].replace(" ", "")           # Limpando de espacos em branco
  modelo_param = parametro_filogenia_clean.split("+")                          # os parametros de Modelos Evolutivos sao MODEL+I+G+F (estes tres ultimos sao os parametros e nao tem ordem definida)
  model_only = str(modelo_param[0])
  print model_only
  return model_only

def paramMoveFilesModelgenerator(dirin, dirincurrent):
  print "\tMoving modelgenerator0.out and *.sh files " + "from " + dirincurrent + " to " + dirin 
  found = False
  for file_move in os.listdir(dirincurrent):
    if file_move.endswith('.out'):
      found  = True
      sh.move(file_move, dirin)						
    if file_move.endswith('.sh'):
      found  = True
      sh.move(file_move, dirin)
  if found is False:
    print "There is not modelgenerator.out and files.sh"
    sys.exit(2)
  
def paramModuleModelgenerator(dirin):
  found = False
  # Executando o modelgenerator do shell
  for m in os.listdir(dirin):
    if m.endswith('.aln'):
    #original if m.endswith('.mafft'):
      found  = True
      #originais path_mafft = os.path.join(dirin, m)
      #originais os.chmod(path_mafft, 0755)  # Assume it's a file
      path_aln = os.path.join(dirin, m)
      os.chmod(path_aln, 0755)  # Assume it's a file
  
      print "Building the Modelgenerator file"
      #original cmd_mg = "java -jar /usr/local/modelgenerator/modelgenerator.jar " + path_mafft + " 6 " 
      cmd_mg = "java -jar modelgenerator.jar " + path_aln + " 6 " 
      handle_mg = os.popen(cmd_mg, 'r', 1)
      for line_mg in handle_mg:
        print line_mg,
      handle_mg.close()
  if found is False:
    print "There is not a '*.aln' alignment file"
    sys.exit(2)

  dirincurrent = os.getcwd( )
  print dirincurrent
  for mg in os.listdir(dirincurrent):
    if mg.endswith('.out'):
      found  = True
      path_mg = os.path.join(dirincurrent, mg)
      os.chmod(path_mg, 0755)  # Assume it's a file
      print dirin
      print dirincurrent
      print "\tWas created " + mg + " in " + dirincurrent
      #Chamando def paramCleanModelgenerator
      model=paramCleanModelgenerator(dirincurrent, mg)  
      #Chamando def paramMoveFilesModelgenerator
      paramMoveFilesModelgenerator(dirin, dirincurrent)
  if found is False:
    print "\tWas not created " + mg + " in " + dirincurrent
    sys.exit(2)

  return model
