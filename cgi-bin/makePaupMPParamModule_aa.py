#! /usr/bin/env python

#TITULO             : PaupMP: Parametros de MP usando PAUP
#AUTOR              : Kary Soriano
#DATA               : 22/01/2008
#DIFICULDADE        : 1
# ==============================================================================
# Objetivo do script: Executado do profile_phylogeny_aa.py
#                     Executa Parametros do Paup para MP
# ==============================================================================
# Data da ultima alteracao do script: 	24/01/2008
#					21/01/2008
# ==============================================================================
#-------------------------------------------------------------------------------
# declarando os modulos a usar 
#-------------------------------------------------------------------------------
import os, shutil as sh
#-------------------------------------------------------------------------------
def ModulePaupMP(dirin, bootstrap):
  btp = str(bootstrap)

  for f in os.listdir(dirin):
    if f.endswith('_nxs'):                                                    
      path_nexus_corrected = os.path.join(dirin, f)
      os.chmod(path_nexus_corrected, 0755)                                                #Assume it's a file
      #usando o modulo paramModule
      import makePaupMPParamModule_aa 
      makePaupMPParamModule_aa.paramModulePaupMP(dirin, path_nexus_corrected, btp)
      break

def paramModulePaupMP(dirin, path_nexus_corrected, btp):
  #------------------------------------------------------------
  # Executando Parametros do MP usando PAUP
  #------------------------------------------------------------
  #1.- paupMP: Maximum Parsimony: Parameter status
  #Attention: paupMP not contain consistency for evolutionary models (ia Modelgenerator)
  #Criando arquivo param_paupMP
  arq_param = dirin + "/param_paupMP" 
  p = file(arq_param, "w")
  p.write('log file=' + dirin + '/LogPaupMpTree_aa.log;\n')			#ou antes ver teste
  p.write('execute ' + path_nexus_corrected + ';\n')
  p.write('set criterion=Parsimony ShowAbbrev=yes ShowTaxNum=yes TaxLabels=full StoreBrLens=yes StoreTreeWts=yes;\n')
  p.write('bootstrap search=heuristic nreps=' + btp + ' Format=Nexus BrLens=yes treefile=bootstrap_aa.mp.bp.nxs replace=yes;\n')
  p.write('pscores;\n')
  p.write('describetrees 1/plot=phylogram brlens=yes;\n')
  p.write('savetrees from=1 to=1 format=nexus maxdecimals=0 savebootp=both replace=yes root=yes file=' + path_nexus_corrected + '_aa.mp.tree.nxs;\n')
  p.write('savetrees from=1 to=1 format=phylip maxdecimals=0 savebootp=both replace=yes root=yes file=' + path_nexus_corrected + '_aa.mp.tree.phy;\n')
  p.write('log stop;\n')
  p.write('q;\n')
  p.close()
  
  print 'File param_paupMP was created in:\n' + dirin

  #2.- paupMP: Maximum Parsimony: Execution status
  #foram usados para todos os casos das execucoes de todos os scripts, a linha de comando em extenso, pode ser usado os alias fornecidos com o programa
    #1 Builds the command line with a program name and the arguments.
    #2 Runs the command and stores a handle in the handle variable. A handle for a command is the same kind of objects as a file handle: you open it (with the popen command, read from it, and close it.
    #3 Reads all the lines from the handle, and prints the joint result. 
  cmd_mp_paup = "paup -n < " + arq_param
  handle_mp_paup = os.popen(cmd_mp_paup, 'r', 1)
  for line_mp_paup in handle_mp_paup:
    print line_mp_paup,
  handle_mp_paup.close()
  
  #4.-Moving file bootstrap for $dirin for organized results
#  sh.move('bootstrap_aa.mp.bp.nxs', dirin)						# movendo o arquivo bootstrap para o subdiretorio principal dirin
  
  print 'The execution has been finished with sucess'
