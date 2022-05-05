#! /usr/bin/env python

# TITULO            : PaupML: Construcao de Arvores filogeneticas por Maxima verossimilhanca
# AUTOR             : Kary Soriano
# DATA              : 15/01/2008
# DIFICULDADE       : 1
# ==============================================================================
# Objetivo do script: Executado do myscript_nucl.py
#                     Executa PaupML
# ==============================================================================
# Data da ultima alteracao do script: 	24/01/2008
# ==============================================================================
#-------------------------------------------------------------------------------
# declarando os modulos a usar 
#-------------------------------------------------------------------------------
import sys, os, re
import shutil as sh
#-------------------------------------------------------------------------------
def ModulePaupML(dirin, model, bootstrap, nb_categ, rates_paup_ml_nucl, alpha, invar):
  mod = str(model)
  btp = str(bootstrap)
  nbc = str(nb_categ)
  rat = str(rates_paup_ml_nucl)
  alp = str(alpha)
  inv = str(invar)

  for f in os.listdir(dirin):
    if f.endswith('_nxs'):                                                    
      path_nexus_corrected = os.path.join(dirin, f)
      os.chmod(path_nexus_corrected, 0755)                                      #Assume it's a file

  #MrBayes Parameters: Comparing and searching Modelgenerator evolutionary models for nucleotides
  #Attention: MrBayes and Modelgenerator have different evolutionary models 
  #Verificando se o modelo evolutivo eleito e um dos parametros do MrBayes
  #Pertencem a MG nucleotides (param_model_evol): JC F81 HKY K80 SYM GTR TrN TrNef TVM TVMef TIM TIMef K81uf K81
  #Pertencem a MB: modelMB, "This parameter sets the rate matrix for nucleotides data"
  mydict_modelMBnst = {'JC':'1','JC69':'1','F81':'1','K80':'2','HKY':'2','HKY85':'2','TrN':'6','K3P':'6','TIM':'6','TVM':'6','SYM':'6','GTR':'6'}
  #1.- paupML: Se o modelo paupML bate com MG
  for x in mydict_modelMBnst.keys():                                                          #make a slice copy of the entire list
    m = re.match(mod + "$", x, re.IGNORECASE)             #Usando so se o modelMG e identico com versao! do contrario usar #m = re.match(modelMG + "*", x, re.IGNORECASE)
    if m:
      found  = True
      modelHit = repr(x).split("\'")
      print "modelMG => ", mod, ", modelpaupML => ", modelHit[1]                      #print "modelMB => ", repr(x), ", modelMG => ", repr(m.group(0))
      print "Executing paupML using modelMG - ModelpaupML =>", modelHit[1],"\n\n";
      #usando o modulo paramModule do paupML
      import makePaupMLParamModule_nucl
      makePaupMLParamModule_nucl.paramModulePaupML(dirin, path_nexus_corrected, mydict_modelMBnst[modelHit[1]], btp, nbc, rat, alp, inv)
      
      #2.- paupML: Se o modelo WB nao bate com MG, usando o modelo poisson default de WB
  if found is False:
    print "modelMG => ", mod, ", modelMB => ", "No hit"
    print "No found evolutionary modelMG consistent in ModelpaupML"
    print "Executing paupML using default modelpaupML - JC  => modelpaupML['JC']\n";
    #usando o modulo paramModule
    import makePaupMLParamModule_nucl
    makePaupMLParamModule_nucl.paramModulePaupML(dirin, path_nexus_corrected, mydict_modelMBnst['JC'], btp, nbc, rat, alp, inv)

