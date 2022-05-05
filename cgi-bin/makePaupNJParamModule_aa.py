#! /usr/bin/env python
#TITULO             : PaupNJ: Parametros de NJ usando PAUP
#AUTOR              : Kary Soriano
#DATA               : 22/01/2008
#DIFICULDADE        : 1
# ==============================================================================
# Objetivo do script: Executado do profile_phylogeny_aa.py
#                     Executa Parametros do Paup para NJ
# ==============================================================================
# Data da ultima alteracao do script: 	24/01/2008
#					21/01/2008
# ==============================================================================
#-------------------------------------------------------------------------------
# declarando os modulos a usar 
#-------------------------------------------------------------------------------
import os, sys, shutil as sh
#-------------------------------------------------------------------------------
def ModulePaupNJ(dirin, bootstrap):
  btp = str(bootstrap)

  for f in os.listdir(dirin):
    if f.endswith('_nxs'):                                                    
      path_nexus_corrected = os.path.join(dirin, f)
      os.chmod(path_nexus_corrected, 0755)                                                  #Assume it's a file
      #usando o modulo paramModule_aa
      paramModulePaupNJ(dirin, path_nexus_corrected, btp)
      break
    
def paramModulePaupNJ(dirin, path_nexus_corrected, btp):
  #------------------------------------------------------------
  # Executando Parametros do NJ usando PAUP
  #------------------------------------------------------------
  #1.- Mudando de nome e diretorio ao outfile do Seqboot
  os.chdir(dirin)
  currentdirectory = dirin
  cmd = 'pwd'
  os.system(cmd)

  #1.- paupNJ: Neighbor-Joining: Parameter status
  #Attention: paupNJ not contain consistency for evolutionary models for aa (ia Modelgenerator)
  #Criando arquivo param_paupNJ
  arq_param = dirin + "/param_paupNJ" 
  p = file(arq_param, "w")
  p.write('log file=' + dirin + '/LogPaupNJTree_aa.log;\n')                              #ou antes ver teste
  p.write('execute ' + path_nexus_corrected + ';\n')
  p.write('set criterion=distance ShowAbbrev=yes ShowTaxNum=yes TaxLabels=full StoreBrLens=yes StoreTreeWts=yes;\n')
  p.write('nj treefile=' + path_nexus_corrected + '_nj_aa_originaltree brlens=yes;\n')
  p.write('bootstrap format=nexus search=nj nreps=' + btp + ' BrLens=yes treefile=bootstrap.nj.bp.nxs replace=yes;\n')
  p.write('dscores 1/objective=lsfit power=0;\n')  
  p.write('describetrees 1/plot=phylogram brlens=yes;\n')  
  p.write('savetrees from=1 to=1 format=nexus maxdecimals=0 savebootp=both replace=yes root=yes file=' + path_nexus_corrected + '.nj.tree.nxs;\n')
  p.write('savetrees from=1 to=1 format=phylip maxdecimals=0 savebootp=both replace=yes root=yes file=' + path_nexus_corrected + '.nj.tree.phy;\n') 
  p.write('log stop;\n')
  p.write('q;\n')
  p.close()
  
  print 'File param_paupNJ was created in:\n' + dirin
  
  #2.- paupNJ: Neighbor-Joining: Execution status
  #foram usados para todos os casos das execucoes de todos os scripts, a linha de comando em extenso, pode ser usado os alias fornecidos com o programa
    #1 Builds the command line with a program name and the arguments.
    #2 Runs the command and stores a handle in the handle variable. A handle for a command is the same kind of objects as a file handle: you open it (with the popen command, read from it, and close it.
    #3 Reads all the lines from the handle, and prints the joint result. 
#  cmd_nj_paup = "paup -n < " + arq_param
  cmd_nj_paup = "paup -n < " + arq_param
  handle_nj_paup = os.popen(cmd_nj_paup, 'r', 1)
  for line_nj_paup in handle_nj_paup:
    print line_nj_paup,
  handle_nj_paup.close()

  #  Mudando de nome e diretorio ao outfile do Seqboot
  cache_location = dirin + "/param_paupNJ"
  if not (cache_location):
    os.mkdir(dirin + "/param_paupNJ")
  else: 
#    sh.move(dirin + "/outfile", path_phylip_corrected + "_phylipnj.seqboot")
#   cmd = 'ls -lh'
#   os.system(cmd)
    print "exist"


   
  #4.-Moving file bootstrap for $dirin for organized results
#  sh.move('bootstrap_aa.nj.bp.nxs', dirin)
  
  print 'The execution has been finished with sucess'


       
