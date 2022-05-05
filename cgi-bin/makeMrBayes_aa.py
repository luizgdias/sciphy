#! /usr/bin/env python

# TITULO            : MrBayes: Construcao de Arvores filogeneticas por Infererencia Bayesiana
# AUTOR             : Kary Soriano
# DATA              : 15/01/2008
# DIFICULDADE       : 1
# ==============================================================================
# Objetivo do script: Executado do profile_phylogeny_aa.py
#                     Executa MrBayes
# (VIVAX)           : python makeMrBayes_aa.py /disk1/home/kary/d_06/projeto/script/script_aa_pipeline/python/fasta/rh blosum62
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

  #MrBayes Parameters: Comparing and searching Modelgenerator evolutionary models 
  #Attention: MrBayes and Modelgenerator have different evolutionary models 
  #Verificando se o modelo evolutivo eleito e um dos parametros do MrBayes
  #Pertencem a MG (param_model_evol): BLOSUM62 CPREV Dayhoff JTT MTREV24  VT WAG DCMut RtREV MtMam
  #Pertencem a MB: modelMB, "This parameter sets the rate matrix for amino acid data"
  modelMB = ['poisson','jones','Dayhoff','MTREV','MtMam','WAG','rtrev','CPREV','VT','BLOSUM','equalin','gtr']
  #1.- MRBAYES: Se o modelo MB bate com MG
  found = False
  for x in modelMB[:]:                                                          #make a slice copy of the entire list
    m = re.match(mod + "$", x, re.IGNORECASE)             #Usando so se o modelMG e identico com versao! do contrario usar #m = re.match(modelMG + "*", x, re.IGNORECASE)
    if m:
      found  = True
      modelHit = repr(x).split("'");
      print "5.1 Executing MrBayes using modelMG - ModelMB =>", modelHit[1]
      print "  modelMG => ", mod, ", modelMB => ", modelHit[1],"\n";                     #print "modelMB => ", repr(m), ", modelMG => ", repr(m.group(0))
      import makeMrBayesParamModule_aa
      makeMrBayesParamModule_aa.paramModuleMrBayes(dirin, path_nexus_corrected, modelHit[1], gen, nbc, pfr, sfr, nch, bur, run, rat)

  #2.- MRBAYES: Se o modelo MB nao bate com MG, usando o modelo poisson default de MB
  if found is False:
    print "modelMG => ", mod, ", modelMB => ", "No hit"
    print "No found evolutionary modelMG consistent in ModelMB"
    print "Executing MrBayes using default modelMB =>", modelMB[0], "\n\n";
    #usando o modulo paramModule
    import makeMrBayesParamModule_aa
    makeMrBayesParamModule_aa.paramModuleMrBayes(dirin, path_nexus_corrected, modelMB[0], gen, nbc, pfr, sfr, nch, bur, run, rat)

