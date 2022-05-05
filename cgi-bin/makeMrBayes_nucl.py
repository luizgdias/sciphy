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
def ModuleMrBayes(dirin, model, ngeneration, nb_categ, printfreq, samplefreq, nchains, burnin, nruns, lset_rates):
  gen = str(ngeneration)
  mod = str(model)
  nbc = str(nb_categ)
  pfr = str(printfreq)
  sfr = str(samplefreq)
  nch = str(nchains)
  bur = str(burnin)
  run = str(nruns)
  rat = str(lset_rates)

  for f in os.listdir(dirin):
    if f.endswith('_nxs'):                                                    
      path_nexus_corrected = os.path.join(dirin, f)
      os.chmod(path_nexus_corrected, 0755)                                      #Assume it's a file

  #MrBayes Parameters: Comparing and searching Modelgenerator evolutionary models for nucleotides
  #Attention: MrBayes and Modelgenerator have different evolutionary models 
  #Verificando se o modelo evolutivo eleito e um dos parametros do MrBayes
  #Pertencem a MG nucleotides (param_model_evol): JC F81 HKY K80 SYM GTR TrN TrNef TVM TVMef TIM TIMef K81uf K81
  #Pertencem a MB: modelMB, "This parameter sets the rate matrix for nucleotides data"
  mydict_modelMBnst = {'JC':1,'JC69':1,'F81':1,'K80':2,'HKY':2,'HKY85':2,'TrN':6,'K3P':6,'TIM':6,'TVM':6,'SYM':6,'GTR':6}
  #1.- MRBAYES: Se o modelo MB bate com MG
  for x in mydict_modelMBnst.keys():                                                          #make a slice copy of the entire list
    m = re.match(mod + "$", x, re.IGNORECASE)             #Usando so se o modelMG e identico com versao! do contrario usar #m = re.match(modelMG + "*", x, re.IGNORECASE)
    if m:
      found  = True
      modelHit = repr(x).split("\'")
      print "modelMG => ", mod, ", modelMB => ", modelHit[1]                      #print "modelMB => ", repr(x), ", modelMG => ", repr(m.group(0))
      print "Executing mrbayes using modelMG - ModelMB =>", modelHit[1],"\n\n";
      #usando o modulo paramModule do MrBayes
      import makeMrBayesParamModule_nucl
      ###makeMrBayesParamModule_nucl.paramModuleMrBayes(dirin, path_nexus_corrected, modelHit[1], gen, nbc, pfr, sfr, nch, bur, run, rat)
      makeMrBayesParamModule_nucl.paramModuleMrBayes(dirin, path_nexus_corrected, mydict_modelMBnst[x], gen, nbc, pfr, sfr, nch, bur, run, rat)
      
      #2.- WEIGHBOR: Se o modelo MB nao bate com MG, usando o modelo poisson default de MB
  if found is False:
    print "modelMG => ", mod, ", modelMB => ", "No hit"
    print "No found evolutionary modelMG consistent in ModelMB"
    print "Executing mrbayes using default modelMB - JC  => modelMB['JC']\n";
    #usando o modulo paramModule
    import makeMrBayesParamModule_nucl
    makeMrBayesParamModule_nucl.paramModuleMrBayes(dirin, path_nexus_corrected, mydict_modelMBnst['JC'], gen, nbc, pfr, sfr, nch, bur, run, rat)

