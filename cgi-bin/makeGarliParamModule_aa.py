#! /usr/bin/env python

#TITULO             : Garli: Parametros do file garli.conf
#AUTOR              : Kary Soriano
#DATA               : 15/01/2008
#DIFICULDADE        : 1
# ==============================================================================
# Objetivo do script: Executado do myscript_aa.py
#                     Executa Paramtros param e sumt_param do MrBayes 
# ==============================================================================
# Data da ultima alteracao do script: 	28/10/2008
# ==============================================================================
#-------------------------------------------------------------------------------
# declarando os modulos a usar 
#-------------------------------------------------------------------------------
import os, re
import shutil as sh
#-------------------------------------------------------------------------------
def paramModuleGarli(dirin, path_nexus_corrected, model, bootstrap, nb_categ):
      mod = str(model)
      btp = str(bootstrap)
      nbc = str(nb_categ)

  #Mudando de nome e diretorio ao outfile do Seqboot
      os.chdir(dirin)
      currentdirectory = dirin

  #------------------------------------------------------------
  # Executando Parametros do Garli 
  #------------------------------------------------------------
  #1.- GARLI: Maximum Likelihood: Parameter status
  # Trabalhando com o diretorio script onde esta o garli.conf 
###  currentdirectory = os.getcwd( )
      print '1'
      print dirin
###  found = False
###  for conf in os.listdir(currentdirectory):
###  for conf in os.listdir(dirin):
      print '2'
###  if not conf.endswith('.conf'):
#      found  = True
      #EEfound  = False
      print 'kary'
  # Verificando o garli.conf
###      arq_garli_conf = currentdirectory + "/garli.conf"
      arq_garli_conf = dirin + "/garli.conf"
      #garli_conf_in = open(arq_garli_conf,"r")
###      garli_conf = open(arq_garli_conf).read()


  # Verificando parametros
      p1 = "[general]" + "\n"
      datafname = "datafname = " + dirin + "/filein.aln_nxs" + "\n"                  #variavel
      #ofprefix = "ofprefix = " + path_nexus_corrected + "_garliout" + "\n"      #variavel
      ofprefix = "ofprefix = " + dirin + "/filein.aln_nxs_garliout" + "\n"      #variavel
      p4 = "streefname = stepwise" + "\n"                                       #streefname = (random, stepwise, <filename>)  Specifies where the starting tree topology and/or model parameters will come from.
      p5 = "attachmentspertaxon = 10" + "\n" 
      p6 = "constraintfile = none" + "\n" 
      searchreps = "searchreps = 1" + "\n"                                      #variavel
      outgroup = "outgroup = 1" + "\n"                                          #variavel
      p9 = "collapsebranches = 1" + "\n\n" 
      p10 = "outputeachbettertopology = 1" + "\n"
      p11 = "outputcurrentbesttree = 1" + "\n\n"
      p12 = "enforcetermconditions = 1" + "\n"
      p13 = "genthreshfortopoterm = 5000" + "\n"
      p14 = "scorethreshforterm = 0.05" + "\n"
      p15 = "significanttopochange = 0.01" + "\n\n"
      p16 = "writecheckpoints = 0" + "\n"
      p17 = "restart = 0" + "\n\n"
      datatype = "datatype = aminoacid" + "\n"                                  #variavel, #datatype = (nucleotide, aminoacid, codon-aminoacid, codon)datatype = (nucleotide, aminoacid, codon-aminoacid, codon)
      ratematrix = "ratematrix = " + mod + "\n"                                 #variavel, #ratematrix = (1rate, 2rate, 6rate, fixed, custom string) The number of relative substitution rate parameters (note that the number of free parameters is this value minus one). Equivalent to the 'nst'
      p20 = "statefrequencies = estimate" + "\n"			        #statefrequencies = (equal, empirical, estimate, fixed)
      paramMB3 = "ratehetmodel = gamma" + "\n"                                  #variavel, ratehetmodel = (none, gamma, gammafixed), numratecats = (1 to 20, 4), invariantsites = (none, estimate, fixed)
      paramMB4 = "numratecats = "+ nbc + "\n"
      paramMB5 = "invariantsites = estimate" + "\n\n"
      p22 = "randseed = -1" + "\n"
      p23 = "availablememory = 512" + "\n"
      p24 = "logevery = 10" + "\n"
      p25 = "saveevery = 100" + "\n"
      p26 = "refinestart = 1" + "\n"
      p27 = "outputphyliptree = 1" + "\n"
      p28 = "outputmostlyuselessfiles = 0" + "\n\n"
      p29 = "[master]"+ "\n"
      bootstrapreps = "bootstrapreps = "+ btp + "\n\n"                              #variavel
      p31 = "nindivs = 4" + "\n"
      p32 = "holdover = 1" + "\n"
      p33 = "selectionintensity = .5" + "\n"
      p34 = "holdoverpenalty = 0" + "\n"
#      p35 = "stopgen = 5000000" + "\n"
#      p36 = "stoptime = 5000000" + "\n\n"
      p35 = "stopgen = 500" + "\n"
      p36 = "stoptime = 500" + "\n\n"
      p37 = "startoptprec = .5" + "\n"
      p38 = "minoptprec = .01" + "\n"
      p39 = "numberofprecreductions = 2" + "\n"
      p40 = "treerejectionthreshold = 20.0" + "\n"
      p41 = "topoweight = 1.0" + "\n"
      p42 = "modweight = .05" + "\n"
      p43 = "brlenweight = 0.2" + "\n"
      p44 = "randnniweight = 0.1" + "\n"
      p45 = "randsprweight = 0.3" + "\n"
      p46 = "limsprweight =  0.6" + "\n"
      p47 = "intervallength = 100" + "\n"
      p48 = "intervalstostore = 5" + "\n\n"
      p49 = "limsprrange = 6" + "\n"
      p50 = "meanbrlenmuts = 5" + "\n"
      p51 = "gammashapebrlen = 1000" + "\n"
      p52 = "gammashapemodel = 1000" + "\n"
      p53 = "uniqueswapbias = 0.1" + "\n"
      p54 = "distanceswapbias = 1.0" + "\n\n"
      p55 = "inferinternalstateprobs = 0" + "\n"

      parameters = [p1,datafname,ofprefix,p4,p5,p6,searchreps,outgroup,p9,p10,p11,p12,p13,p14,p15,p16,p17,datatype,ratematrix,p20,paramMB3,paramMB4,paramMB5,p22,p23,p24,p25,p26,p27,p28,p29,bootstrapreps,p31,p32,p33,p34,p35,p36,p37,p38,p39,p40,p41,p42,p43,p44,p45,p46,p47,p48,p49,p50,p51,p52,p53,p54,p55]
      all = "".join(parameters)

      #Escrevendo o arquivo de saida
      garli_conf=file(arq_garli_conf, 'w')
      garli_conf.write(all)
      garli_conf.close()
###      os.chmod(garli_conf, 0755)
#      garli_conf = file(arq_garli_conf, 'w')
#  if found is False:
#    print "There is not a garli.conf"
  
  #2.- GARLI: Maximum Likelihood: Execution status
  #foram usados para todos os casos das execucoes de todos os scripts, a linha de comando em extenso, pode ser usado os alias fornecidos com o programa
    #1 Builds the command line with a program name and the arguments.
    #2 Runs the command and stores a handle in the handle variable. A handle for a command is the same kind of objects as a file handle: you open it (with the popen command, read from it, and close it.
    #3 Reads all the lines from the handle, and prints the joint result. 
  
  #3.- Executando parametros MrBayes
      ###cmd_mb_p = "garli"
       
      cmd_mb_p = "Garli0.96b8 " + dirin + "/garli.conf"  
      handle_p = os.popen(cmd_mb_p, 'r', 1)
      for line_p in handle_p:
        print line_p,
      handle_p.close()

  #4.- Executando parametros Consense
  # Criando arquivo param_consense
###  arq_param_c = currentdirectory + "/" + dirin + "/param_consense"
      arq_param_c = dirin + "/param_consense"  
      c = file(arq_param_c, "w")
#      c.write(path_nexus_corrected + '_garliout.boot.phy\n')
      c.write(dirin + '/filein.aln_nxs_garliout.boot.phy\n')
      c.write('O\n')
      c.write('1\n')
      c.write('R\n')
      c.write('Y\n')
      c.close()
  
      print 'Executando Consense...\n'
      cmd_c = "phylip consense < " + arq_param_c
      handle_c = os.popen(cmd_c, 'r', 1)
      for line_c in handle_c:
        print line_c,
      handle_c.close()
      #Mudando de nome e diretorio ao outfile do Consense
      os.mkdir(dirin+"/outfile")
      os.mkdir(dirin+"/outtree")
#original      sh.move(dirin + "/outfile", path_nexus_corrected + "_garli.consenseout")
#original      sh.move(dirin + "/outtree", path_nexus_corrected + "_garli.consensetree")
      sh.move(dirin + "/outfile", path_nexus_corrected + "_garli.consenseout")
      sh.move(dirin + "/outtree", path_nexus_corrected + "_garli.consensetree")
    
 
      print 'The execution has been finished with sucess'
  
#------------------------------------------------------------
 
      
#1.- Procurar o garli.conf

#2.- Editar o garli.conf
#     2a.-General file
#            datafname = murphy29.rag1rag2.nex
#            ofprefix = OUTPUT_PREFIX
#            searchreps = 1
#            outgroup = 1
#           General evolutionary models
#            datatype = dna
#            ratematrix = 6rate
#            statefrequencies = equal
#            ratehetmodel = gamma
#            numratecats = 4
#            invariantsites = estimate
#           Master
#           bootstrapreps = 200 or 500
