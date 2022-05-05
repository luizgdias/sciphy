#! /usr/bin/env python

# TITULO           : RAxML: Parametros de ML usando RAxML
# AUTOR            : Kary Soriano
# DATA             : 03/11/2008
# DIFICULDADE      : 1
# http://icwww.epfl.ch/~stamatak/index-Dateien/Page443.htm
# ==============================================================================
# Objetivo do script: Executado do my_script_aa.py | Executa Parametros de RAxML para ML
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
def ModuleRaxml(dirin, model, bootstrap, nb_categ, rates_raxml_aa, freq_raxml_aa):
  btp = str(bootstrap)
  mod = str(model)
  nbc = str(nb_categ)
  rat = str(rates_raxml_aa)
  fre = str(freq_raxml_aa)

  mydict_modelRAXML = ['DAYHOFF', 'DCMUT', 'JTT', 'MTREV', 'WAG', 'RTREV', 'CPREV', 'VT', 'BLOSUM62', 'MTMAM', 'GTR']                                                #a versao VI e usado HKY85
  #mydict_paramRAXML = {"PC":"PROTCAT", "PM":"PROTMIX", "PG":"PROTGAMMA", "PCG":"PROTCAT_GAMMA", "PGI":"PROTGAMMAI", "PMI":"PROTMIXI", "PCGI":"PROTCAT_GAMMAI","F":"F"}
    
  #1.- RAXML: Se o modelo RAXML bate com MG
  found = False
  for x in mydict_modelRAXML[:]:
    m = re.match(mod + "$", x, re.IGNORECASE)
    if m:
      found  = True
      modelHit = repr(x).split("'");
      print "param_model_evol => ", mod, ", modelPHYML => ", modelHit[1]   #print "modelPHYML => ", repr(x), ", modelMG => ", repr(m.group(0))
      print "Executing RaxMLPhyml using rates => ", rat, ", model => ", modelHit[1], ", frequency => ", fre, "\n\n";
      #usando o modulo paramModule do MrBayes
      import makeRaxmlParamModule_aa
      result = makeRaxmlParamModule_aa.paramModuleRaxml(dirin, modelHit[1], rat, fre, btp, nbc)
      #break

  #2.- RAXML: Se o modelo RAXML nao bate com MG, usando o modelo JC default de RAXML
  if found is False:
    print "5 No found evolutionary modelRaxml and parameterRaxml consistent in ModelRAXML"
    print "  modelMG => ", mod, ", modelRaxml => ", "No hit";
    print "  Executing Raxml using default modelRaxml =>", rat + " " + mydict_modelRAXML[0] + " " + fre +"\n"
    #usando o modulo paramModule
    import makeRaxmlParamModule_aa
    result = makeRaxmlParamModule_aa.paramModuleRaxml(dirin, mydict_modelRAXML[0], rat, fre, btp, nbc)
