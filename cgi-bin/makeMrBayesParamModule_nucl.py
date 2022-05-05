#! /usr/bin/env python

#TITULO             : MrBayes: Parametros e sumpt parametros de MrBayes
#AUTOR              : Kary Soriano
#DATA               : 15/01/2008
#DIFICULDADE        : 1
# ==============================================================================
# Objetivo do script: Executado do myscript_nucl.py
#                     Executa Paramtros param e sumt_param do MrBayes 
# ==============================================================================
# Data da ultima alteracao do script: 	24/01/2008
#					21/01/2008
#                                       15/07/2008
# ==============================================================================
#-------------------------------------------------------------------------------
# declarando os modulos a usar 
#-------------------------------------------------------------------------------
import os
#-------------------------------------------------------------------------------
def paramModuleMrBayes(dirin, path_nexus_corrected, model, ngeneration, nb_categ, printfreq, samplefreq, nchains, burnin, nruns, lset_rates):
  gen = str(ngeneration)
  mod = str(model)
  nbc = str(nb_categ)
  pfr = str(printfreq)
  sfr = str(samplefreq)
  nch = str(nchains)
  bur = str(burnin)
  run = str(nruns)
  rat = str(lset_rates)

  #------------------------------------------------------------
  # Executando Parametros do MrBayes 
  #------------------------------------------------------------
  #1.- MRBAYES: Bayesian Inference: Parameter status
  #Criando arquivo param_mrbayes
  arq_param = dirin + "/param_mrbayes" 
  p = file(arq_param, "w")
  p.write('log start filename=' + dirin + '/mbout_param_nucl.log replace;\n')
  p.write('set autoclose=yes nowarn=yes;\n')
  p.write('execute ' + path_nexus_corrected + ';\n')
  ###p.write('outgroup 1\n')							#outgroup <number>/<taxon name>
  p.write('matrix;\n')
  p.write('lset nst='+ mod +' rates='+ rat +';\n') 
  p.write('mcmcp ngen='+gen+' printfreq='+pfr+' samplefreq='+sfr+' nchains='+nch+' savebrlens=yes startingtree=random Stoprule=yes filename=' + path_nexus_corrected + '.mb.out;\n')
  p.write('mcmc;\n')
  p.write('sump filename=' + path_nexus_corrected + '.mb.out printtofile=yes burnin='+bur+';\n') #pode ter problema aqui porque ao por Stoprule=yes como parametro, ele vai parar ao conseguir este estado de convergenciae pode ser que tenhamos que descer o valor de burin ou que termine antes de terminar o numero de geracoes proposto
  p.write('sumt filename=' + path_nexus_corrected + '.mb.out showtreeprobs=yes burnin='+bur+';\n')
#  p.write('sump filename=' + path_nexus_corrected + '_nucl.mb.out burnin=100 printtofile=yes\n') #pode ter problema aqui porque ao por Stoprule=yes como parametro, ele vai parar ao conseguir este estado de convergenciae pode ser que tenhamos que descer o valor de burin ou que termine antes de terminar o numero de geracoes proposto
#  p.write('sumt filename=' + path_nexus_corrected + '_nucl.mb.out burnin=100 showtreeprobs=yes\n')
  p.write('log stop;\n')
  p.write('q;\n')
  p.close()

  print '  Files param_mrbayes and param_sumpt_mrbayes were created in: ' + dirin + "\n"

  #2.- MRBAYES: Bayesian Inference: Execution status
  #foram usados para todos os casos das execucoes de todos os scripts, a linha de comando em extenso, pode ser usado os alias fornecidos com o programa
    #1 Builds the command line with a program name and the arguments.
    #2 Runs the command and stores a handle in the handle variable. A handle for a command is the same kind of objects as a file handle: you open it (with the popen command, read from it, and close it.
    #3 Reads all the lines from the handle, and prints the joint result. 
  
  #3.- Executando parametros MrBayes
  cmd_mb_p = "mb < " + arq_param
  handle_p = os.popen(cmd_mb_p, 'r', 1)
  for line_p in handle_p:
    print line_p,
  handle_p.close()
 
  print 'The execution has been finished with sucess'
  
#------------------------------------------------------------
   
  ###p.write('outgroup Arabidopsis Drosophila Escherichia Synechocystis\n')

  ###p.write('mcmc ngen=10 printfreq=5 samplefreq=5 nchains=4 savebrlens=yes startingtree=random filename=' + path_nexus_corrected + '_nucl.mb.out\n') #alteracao/question script
  ###p.write('mcmc ngen=50000 printfreq=500 samplefreq=100 nchains=4 savebrlens=yes diagnfreq=10000 filename=' + path_nexus_corrected + '.nex.out\n')#question in the script
  #p.write('mcmc ngen=10 printfreq=5 samplefreq=5 nchains=4 savebrlens=yes startingtree=random filename=' + path_nexus_corrected + '.nex.out\n')#question in the script
