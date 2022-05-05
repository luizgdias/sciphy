#! /usr/bin/env python

# TITULO           : GarliML: Parametros de ML usando Garli | versao 096
# AUTOR            : Kary Soriano
# DATA             : 09/09/2008
# DIFICULDADE      : 1
# http://workshop.molecularevolution.org/mbl/software/garli/
# ==============================================================================
# Objetivo do script: Executado do my_script_nucl.py | Executa Parametros do Garli para ML
# Usar o argumento  : Precisa do arquivo garli.conf para execucao
# ==============================================================================
# Data da ultima alteracao do script: 09/09/2008
# ==============================================================================
#-------------------------------------------------------------------------------
# declarando os modulos a usar 
#-------------------------------------------------------------------------------
import sys, os, re
import shutil as sh
#-------------------------------------------------------------------------------
# Abrindo o diretorio: Trabalhando com o arquivo garli.conf
#-------------------------------------------------------------------------------
#def ModuleGarli(dirin, param_model_evol):
def ModuleGarli(dirin, model, bootstrap, nb_categ):
  mod = str(model)
  btp = str(bootstrap)
  nbc = str(nb_categ)
  
  os.putenv("LD_LIBRARY_PATH","/usr/local/ncl-2.1.06/lib/ncl/")

  for f in os.listdir(dirin):
    if f.endswith('_nxs'):
      path_nexus_corrected = os.path.join(dirin, f)
      os.chmod(path_nexus_corrected, 0755)

  mydict_modelGARLInst = {"JC":"1rate","F81":"1rate","K80":"2rate","HKY":"2rate","TrN":"6rate","K3P":"6rate","TIM":"6rate","TVM":"6rate","SYM":"6rate","GTR":"6rate"}
#  mydict_paramGARLI = {"G":"ratehetmodel = gamma", "I":"invariantsites = estimate", "NoneGamma":"ratehetmodel = none", "NoneI":"invariantsites = none"}     #Vamos trabalhar com gamma e com invariant estimados
  #1.- GARLI: Se o modelo GARLI bate com MG

#####  mydict_modelMBnst = {"JC":"1","JC69":"1","F81":"1","K80":"2","HKY":"2","HKY85":"2","TrN":"6","K3P":"6","TIM":"6","TVM":"6","SYM":"6","GTR":"6"}
#####  #1.- Garli: Se o modelo MB bate com MG

  found = False  #inserido da versao de aa
  for x in mydict_modelGARLInst.keys():                                                          #make a slice copy of the entire list
    m = re.match(mod + "$", x, re.IGNORECASE)             #Usando so se o modelMG e identico com versao! do contrario usar #m = re.match(modelMG + "*", x, re.IGNORECASE)
    if m:
      found  = True
      modelHit = repr(x).split("\'")
      print "modelMG => ", mod, ", modelGarli => ", modelHit[1]                      #print "modelMB => ", repr(x), ", modelMG => ", repr(m.group(0))
      print "Executing Garli using modelMG - ModelGarli =>", modelHit[1],"\n\n";
      #usando o modulo paramModule do paupML
      import makeGarliParamModule_nucl
      makeGarliParamModule_nucl.paramModuleGarli(dirin, path_nexus_corrected, mydict_modelGARLInst[modelHit[1]], btp, nbc)
      
      #2.- Garli: Se o modelo WB nao bate com MG, usando o modelo poisson default de WB
  if found is False:
    print "modelMG => ", mod, ", modelMB => ", "No hit"
    print "No found evolutionary modelMG consistent in ModelGarli"
    print "Executing paupML using default modelpaupML - JC  => modelGarli['JC']\n";
    #usando o modulo paramModule
    import makeGarliParamModule_nucl
    makeGarliParamModule_nucl.paramModuleGarli(dirin, path_nexus_corrected, mydict_modelGARLInst["JC"], btp, nbc)


