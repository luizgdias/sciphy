#! /usr/bin/env python

# TITULO            : MrBayes: Construcao de Arvores filogeneticas por Infererencia Bayesiana
# AUTOR             : Kary Soriano
# DATA              : 15/01/2008
# DIFICULDADE       : 1
# ==============================================================================
# Objetivo do script: Executado do myscript_nucl.py
#                     Executa MrBayes
# (VIVAX)           : python makeMrBayes_nucl.py /disk1/home/kary/d_06/projeto/script/script_nucl_pipeline/python/fasta/rh blosum62
# ==============================================================================
# Data da ultima alteracao do script: 	24/01/2008
#					21/01/2008
#					18/01/2008
#	   				15/01/2008
# ==============================================================================
#-------------------------------------------------------------------------------
# declarando os modulos a usar 
#-------------------------------------------------------------------------------
import sys, os, re
import shutil as sh
#-------------------------------------------------------------------------------
###dirin = sys.argv[1]								# print "O nome do caminho e arquivo de entrada e: " + dirin_do_ficheiro 
###dirin_arg_pas = sys.argv[1:]			        	  		# print "Os argumentos passados sao: " + str(dirin_arg_pas)
###modelMG = sys.argv[2]
###modelMG_arg_pas = sys.argv[2:]
###print "O nome do diretorio de entrada e o modelMG sao: " + dirin + " " + modelMG
###print "E os argumentos passados sao: " + str(dirin_arg_pas)
def ModuleMrBayes(dirin, param_model_evol):
  for f in os.listdir(dirin):
    if f.endswith('_nxs'):                                                    
      path_nexus_corrected = os.path.join(dirin, f)
      os.chmod(path_nexus_corrected, 0755)                                      #Assume it's a file
      #nexus_corrected = f
  #print "este dirin para MB" + dirin 								#arquivo fasta fora do loop, corrected dentro do loop
  #print nexus_corrected							#arquivo corrected fora do loop
  #print path_nexus_corrected							#dirin + arquivo nexus_corrected
  #print "este modelo para MB" + param_model_evol + f

  #MrBayes Parameters: Comparing and searching Modelgenerator evolutionary models for nucleotides
  #Attention: MrBayes and Modelgenerator have different evolutionary models 
  modelMB = ['JC','F81','K80','HKY','TrN','K3P','TIM','TVM','SYM','GTR']
  paramMB = ['E','G','I','Ad']                        #Equal/Gamma/Propinv/Invgamma/Adgamma
  
    #Verificando se o modelo evolutivo eleito e um dos parametros do MrBayes
    #Pertencem a MG nucleotides (param_model_evol): JC F81 HKY K80 SYM GTR TrN TrNef TVM TVMef TIM TIMef K81uf K81
    #Pertencem a MB: modelMB, "This parameter sets the rate matrix for nucleotides data"
  found = False
  for a in modelMB[:]:                                                          #make a slice copy of the entire list
    m = re.match(param_model_evol[0] + "$", a, re.IGNORECASE)             #Usando so se o modelMG e identico com versao! do contrario usar #m = re.match(modelMG + "*", x, re.IGNORECASE)
    if m:
      #1.- MRBAYES: Se o modelo MB bate com MG
      found  = True
      modelHit = repr(a).split("'");
      print "5 Executing MrBayes using modelMG - ModelMB =>", modelHit[1]
      print "  modelMG => ", param_model_evol[0], ", modelMB => ", modelHit[1],"\n";                      #print "modelMB => ", repr(x), ", modelMG => ", repr(m.group(0))
      
      #2.- Mudando modelMB para parametro lset nst = 1,2,3 do MrBayes
      mydict_modelMBnst = {"JC":"1","F81":"1","K80":"2","HKY":"2","TrN":"6","K3P":"6","TIM":"6","TVM":"6","SYM":"6","GTR":"6"}
      for b in mydict_modelMBnst.keys():
        if param_model_evol[0] == b:
          print mydict_modelMBnst[b]              #agora NST, que e o meu modelo antigo modelMB
      
      #3.- MRBAYES: Se o parametro existe e o passo dele para MrBayes 
      if len(param_model_evol)>1:
        found = False
        for y in paramMB[:]:  
          if len (param_model_evol) == 2:
            n = re.match(param_model_evol[1] + "$", y, re.IGNORECASE)             #Usando so se o modelMG e identico com versao! do contrario usar #m = re.match(modelMG + "*", x, re.IGNORECASE)
            if n:
              found  = True
              paramHitn = repr(y).split("'");
              print "  5.1 Executing MrBayes using paramMG - ParamMB =>", paramHitn[1]
              #Mudando para os modelos lset rates = em Mrbayes Unitarios: G ou I
              mydict_paramMB = {"E":"Equal", "G":"Gamma", "I":"Propinv", "A":"Adgamma"}
              for x in mydict_paramMB.keys():
                if paramHitn[1] == x:
                  #print mydict_paramMB[x]
                  import makeMrBayesParamModule_nucl
                  makeMrBayesParamModule_nucl.paramModuleMrBayes(dirin, path_nexus_corrected, mydict_modelMBnst[b], mydict_paramMB[x])
          if len (param_model_evol) == 3:
              Invgamma  = 'Invgamma'
              print "  5.2 Executing MrBayes using paramMG - ParamMB =>", Invgamma
              #Mudando para os modelos lset rates = em Mrbayes G + I
              import makeMrBayesParamModule_nucl
              makeMrBayesParamModule_nucl.paramModuleMrBayes(dirin, path_nexus_corrected, mydict_modelMBnst[b], Invgamma)

      else:
        print 'There are not evolutionary parameters in modelgenerator '
        myparammodeldefault = 'Equal'
        #usando o modulo paramModule do MrBayes
        import makeMrBayesParamModule_nucl
        makeMrBayesParamModule_nucl.paramModuleMrBayes(dirin, path_nexus_corrected, mydict_modelMBnst[b], myparammodeldefault)
    
          #2.- MRBAYES: Se o modelo MB nao bate com MG, usando o modelo poisson default de MB
  if found is False:
    myparammodeldefault = 'Equal'

    print "No found evolutionary modelMG consistent in ModelMB"
    print "5 Executing MrBayes using default modelMB =>", modelMB[0]
    print "  modelMG => ", param_model_evol, ", modelMB => ", "No hit\n";
    #usando o modulo paramModule
    import makeMrBayesParamModule_nucl
    makeMrBayesParamModule_nucl.paramModuleMrBayes(dirin, path_nexus_corrected, mydict_modelMBnst[b], myparammodeldefault)


