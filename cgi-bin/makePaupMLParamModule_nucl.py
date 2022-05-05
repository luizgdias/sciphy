#! /usr/bin/env python

#TITULO             : PaupML: Parametros de ML usando PAUP
#AUTOR              : Kary Soriano
#DATA               : 10/06/2008
#DIFICULDADE        : 1
# ==============================================================================
# Objetivo do script: Executado do myscript_nucl.py
#                     Executa Parametros do Paup para ML
# ==============================================================================
# Data da ultima alteracao do script: 	10/06/2008
#					//2008
# ==============================================================================
#-------------------------------------------------------------------------------
# declarando os modulos a usar 
#-------------------------------------------------------------------------------
import os, shutil as sh
#-------------------------------------------------------------------------------
def paramModulePaupML(dirin, path_nexus_corrected, model, bootstrap, nb_categ, rates_paup_ml_nucl, alpha, invar):
  mod = str(model)
  btp = str(bootstrap)
  nbc = str(nb_categ)
  rat = str(rates_paup_ml_nucl)
  alp = str(alpha)
  inv = str(invar)
    
  #------------------------------------------------------------
  # Executando Parametros do ML usando PAUP
  #------------------------------------------------------------
  #1.- paupML: Maximum Likelihood: Parameter status
  #Attention: paupML 
  #Criando arquivo param_paupML
  arq_param = dirin + "/param_paupML" 
  p = file(arq_param, "w")
  p.write('log file=' + dirin + '/LogPaupMLTree.log;\n')			#ou antes ver teste
  p.write('execute ' + path_nexus_corrected + ';\n')
  p.write('set criterion=Likelihood ShowAbbrev=yes ShowTaxNum=yes TaxLabels=full StoreBrLens=yes StoreTreeWts=yes;\n')
  p.write('lset nst='+ mod +' Rates='+rat+' Pinvar='+invar+' Ncat='+nbc+' Shape='+alp+';\n')
  #p.write('outgroup 1;\n')
  p.write('bootstrap search=heuristic nreps='+btp+' keepall=yes grpfreq=no Format=Nexus BrLens=yes treefile=bootstrap_nucl.ml.bp.nxs replace=yes;\n')
  p.write('pscores;\n')
  p.write('describetrees 1/plot=phylogram brlens=yes;\n')
  p.write('savetrees from=1 to=1 format=nexus maxdecimals=0 savebootp=both replace=yes root=yes file=' + path_nexus_corrected + '_nucl.ml.tree.nxs;\n')
  p.write('savetrees from=1 to=1 format=phylip maxdecimals=0 savebootp=both replace=yes root=yes file=' + path_nexus_corrected + '_nucl.ml.tree.phy;\n')
  p.write('log stop;\n')
  p.write('q;\n')
  p.close()
  
  print 'File param_paupML was created in:\n' + dirin

  #2.- paupML: Maximum Parsimony: Execution status
  #foram usados para todos os casos das execucoes de todos os scripts, a linha de comando em extenso, pode ser usado os alias fornecidos com o programa
    #1 Builds the command line with a program name and the arguments.
    #2 Runs the command and stores a handle in the handle variable. A handle for a command is the same kind of objects as a file handle: you open it (with the popen command, read from it, and close it.
    #3 Reads all the lines from the handle, and prints the joint result. 
  cmd_ml_paup = "paup -n < " + arq_param
  handle_ml_paup = os.popen(cmd_ml_paup, 'r', 1)
  for line_ml_paup in handle_ml_paup:
    print line_ml_paup,
  handle_ml_paup.close()
  
  #4.-Moving file bootstrap for $dirin for organized results
  sh.move('bootstrap_nucl.ml.bp.nxs', dirin)						# movendo o arquivo bootstrap para o subdiretorio principal dirin

  print 'The execution has been finished with sucess'

#------------------------------------------------------------
    
### For obtain again the consense tree:
###savetrees file=rh.ml.tree.nxs format=nexus brlens=yes root=yes
###gettrees allblocks=yes duptrees=keep storetreewts=yes storebrlens=yes mode=7 file=rh.ml.tree.nxs; SOLO NEXUS
###contree /strict=no majrule=yes usetreewts=yes showtree=yes grpfreq=yes;

  #p.write('hsearch Swap=TBR AddSeq=Random SaveReps=yes nreps=100 start=stepwise;\n')
  #p.write('n;\n')							#aqui deu problema na kineto3
  
  ###p.write('outgroup Arabidopsis Drosophila Escherichia Synechocystis;\n')
  ###p.write('set root=outgroup OutRoot=Monophyl;\n')
  ###p.write('roottrees;\n')
  #p.write('gettrees allblocks=yes duptrees=keep storetreewts=yes storebrlens=yes mode=7 file=bootstrap.ml.bp;\n')	#nexus_corrected.ml.bp = file for bootstrap in ML
  #p.write('Y;\n')
  #p.write('n;\n')
  #p.write('contree /strict=no majrule=yes usetreewts=yes showtree=yes treefile=' + path_nexus_corrected + '.ml.cons grpfreq=yes;\n')	#path_mafft.ml.cons = file for consense bootstrap in ML
  #p.write('log stop;\n')
  ###p.write('savetrees file=' + path_nexus_corrected + '.ml.tree.nxs format=nexus brlens=yes root=yes\n')
  ###p.write('savetrees file=' + path_nexus_corrected + '.ml.tree.phy format=phylip brlens=yes root=yes\n')
