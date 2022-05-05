#! /usr/bin/env python

# TITULO            : Weighbor: Construcao de Arvores filogeneticas
# AUTOR             : Kary Soriano
# DATA              : 31/01/2008
# DIFICULDADE       : 1
# ==============================================================================
# Objetivo do script: Executado do myscript_nucl.py
#                     Executa Weighbor
# (VIVAX)           : 
# ==============================================================================
# Data da ultima alteracao do script: 	31/01/2008
#					//2008
# ==============================================================================
#-------------------------------------------------------------------------------
# declarando os modulos a usar 
#-------------------------------------------------------------------------------
import sys, os, re
import shutil as sh
#-------------------------------------------------------------------------------
def ModuleWeighbor(dirin, model, bootstrap, nb_categ):
  btp = str(bootstrap)
  mod = str(model)
  nbc = str(nb_categ)
  
  for f in os.listdir(dirin):
    if f.endswith('_phy'):                                                    
      path_phylip_corrected = os.path.join(dirin, f)
      os.chmod(path_phylip_corrected, 0755)                                      #Assume it's a file

  #Weighbor Parameters: Comparing and searching Modelgenerator evolutionary models for nucleotides
  #Attention: Weighbor and Modelgenerator have different evolutionary models 
  modelWB = {"HKY" : "", "TN" : "M\n", "GTR" : "M\n\n"}  
    #Verificando se o modelo evolutivo eleito e um dos parametros do Weighbor
    #Pertencem a MG (param_model_evol): BLOSUM62 CPREV Dayhoff JTT MTREV24  VT WAG DCMut RtREV MtMam
    #Pertencem a Weighbor: modelWB, "This parameter sets the rate matrix for amino acid data"
  found = False
  for x in modelWB.keys():                                                          #make a slice copy of the entire list
    m = re.match(mod + "$", x, re.IGNORECASE)             #Usando so se o modelMG e identico com versao! do contrario usar #m = re.match(modelMG + "*", x, re.IGNORECASE)
    if m:
     
      #1.- WEIGHBOR: Se o modelo WB bate com MG
      found  = True
      modelHit = repr(x).split("\'")
      print "modelMG => ", mod, ", modelWB => ", modelHit[1]                      #print "modelMB => ", repr(x), ", modelMG => ", repr(m.group(0))
      print "Executing Weighbor using modelMG - ModelWB =>", modelHit[1],"\n\n";
      #usando o modulo paramModule do MrBayes
      import makeWeighborParamModule_nucl
      makeWeighborParamModule_nucl.paramModuleWeighbor(dirin, path_phylip_corrected, modelHit[1], btp, nbc)

      #2.- WEIGHBOR: Se o modelo WB nao bate com MG, usando o modelo poisson default de WB
  if found is False:
    print "modelMG => ", mod, ", modelWB => ", "No hit"
    print "No found evolutionary modelMG consistent in ModelWB"
    print "Executing Weighbor using default modelWB - HKY  => modelWB['HKY']\n";
    #usando o modulo paramModule
    import makeWeighborParamModule_nucl
    makeWeighborParamModule_nucl.paramModuleWeighbor(dirin, path_phylip_corrected, modelWB['HKY'], btp, nbc)


