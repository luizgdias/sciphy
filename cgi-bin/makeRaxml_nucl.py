#! /usr/bin/env python

# TITULO           : RAxML: Parametros de ML usando RAxML
# AUTOR            : Kary Soriano
# DATA             : 03/11/2008
# DIFICULDADE      : 1
# http://icwww.epfl.ch/~stamatak/index-Dateien/Page443.htm
# ==============================================================================
# Objetivo do script: Executado do my_script_nucl.py | Executa Parametros de RAxML para ML
# Usar o argumento  : Precisa parametros para execucao
# ==============================================================================
# Data da ultima alteracao do script: 03/11/2008
# ==============================================================================
#-------------------------------------------------------------------------------
# declarando os modulos a usar 
#-------------------------------------------------------------------------------
import sys, os, re
import shutil as sh
#-------------------------------------------------------------------------------
# Abrindo o diretorio
#-------------------------------------------------------------------------------
def ModuleRaxml(dirin, model, bootstrap, nb_categ, rates_raxml_nucl):
  btp = str(bootstrap)
  mod = str(model)
  nbc = str(nb_categ)
  rat = str(rates_raxml_nucl)
  
  import makeRaxmlParamModule_nucl
  makeRaxmlParamModule_nucl.paramModuleRaxml(dirin, mod, rat, btp, nbc)

###  mydict_modelRAXML = ['GTR']                                                #a versao VI e usado HKY85
###  mydict_paramRAXML = {"GTRCAT":"GTRCAT", "G":"GTRGAMMA", "GTRMIX":"GTRMIX", "GTRCAT_GAMMA":"GTRCAT_GAMMA", "GTRGAMMAI":"GTRGAMMAI", "I":"GTRMIXI"}
###original
###  #1.- RAXML: Se o modelo RAXML bate com MG
 ### found = False
###  for x in mydict_modelRAXML[:]:
###    m = re.match(mod + "$", x, re.IGNORECASE)
###    if m:
 ###     found  = True
 ###     modelHit = repr(x).split("'");
###      print "param_model_evol => ", mod, ", modelPHYML => ", modelHit[1]   #print "modelPHYML => ", repr(x), ", modelMG => ", repr(m.group(0))
###      print "Executing RaxMLPhyml using model => ", modelHit[1], ", rates => ", rat, "\n\n";
###      #usando o modulo paramModule do MrBayes
 ###     import makeRaxmlParamModule_nucl
###      makeRaxmlParamModule_nucl.paramModuleRaxml(dirin, modelHit[1], rat, btp, nbc)
###      #break

  #2.- RAXML: Se o modelo RAXML nao bate com MG, usando o unico modelo GTR default de RAXML
###  if found is False:
###    print "5 No found evolutionary modelRaxml and parameterRaxml consistent in ModelRAXML"
###    print "  modelMG => ", mod, ", modelRaxml => ", "No hit";
###    print "  Executing Raxml using default modelRaxml =>", mydict_modelRAXML[0] + " " + rat +"\n"
###    #usando o modulo paramModule
###    import makeRaxmlParamModule_nucl
###    makeRaxmlParamModule_nucl.paramModuleRaxml(dirin, mydict_modelRAXML[0], rat, btp, nbc)

