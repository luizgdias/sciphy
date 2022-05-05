#! /usr/bin/env python

# TITULO            : Phyml: Construcao de Arvores filogeneticas por Maxima Verossimilhanca
# AUTOR             : Kary Soriano
# DATA              : 31/01/2008
# DIFICULDADE       : 1
# ==============================================================================
# Objetivo do script: Executado do profile_phylogeny_aa.py
#                     Executa Phyml
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
def ModulePhyml(dirin, model, bootstrap, nb_categ, alpha, invar):
  btp = str(bootstrap)
  mod = str(model)
  inv = str(invar)
  nbc = str(nb_categ)
  alp = str(alpha)

  for f in os.listdir(dirin):
    if f.endswith('_phy'):                                                    
      path_phylip_corrected = os.path.join(dirin, f)
      os.chmod(path_phylip_corrected, 0755)                                     # Assume it's a file
  
      #Phyml Parameters: Comparing and searching Modelgenerator evolutionary models 
      #Attention: Phyml and Modelgenerator have different evolutionary models 
      modelPHYML = ['JTT','MtREV','WAG','DCMut','RtREV','CpREV','VT','Blosum62','MtMam','Dayhoff']
        #Verificando se o modelo evolutivo eleito e um dos parametros do Phyml
        #Pertencem a MG (param_model_evol): BLOSUM62 CPREV Dayhoff JTT MTREV24  VT WAG DCMut RtREV MtMam
        #Pertencem a PHYML: modelPHYML, "This parameter sets the rate matrix for amino acid data"
      found = False
      for x in modelPHYML[:]:                                                       # make a slice copy of the entire list
        m = re.match(mod + "$", x, re.IGNORECASE)                      # Usando so se o modelMG e identico com versao! do contrario usar #m = re.match(modelMG + "*", x, re.IGNORECASE)
        if m:
          #1.- PHYML: Se o modelo PHYML bate com MG
          found  = True
          modelHit = repr(x).split("'");
          print "param_model_evol => ", mod, ", modelPHYML => ", modelHit[1]   #print "modelPHYML => ", repr(x), ", modelMG => ", repr(m.group(0))
          print "Executing Phyml using modelMG - ModelPHYML =>", modelHit[1],"\n\n";
          #usando o modulo paramModule do Phyml
          cmd_phyml = "phyml_linux "+path_phylip_corrected+" 1 i 1 "+btp+" "+modelHit[1]+" "+inv+" "+nbc+" "+alp+" "+" BIONJ n n"
          handle_phyml = os.popen(cmd_phyml, 'r', 1)
          for line_phyml in handle_phyml:
            print line_phyml,
          handle_phyml.close()
      
      ###    #2.- PHYML: Se o modelo PHYML nao bate com MG, usando o modelo poisson default de PHYML
      if found is False:
        print "modelMG => ", mod, ", modelPHYML => ", "No hit"
        print "No found evolutionary modelMG consistent in ModelPHYML"
        print "Executing Phyml using default modelPHYML =>", modelPHYML[0], "\n\n";
        #usando o modulo paramModule
        cmd_phyml = "phyml_linux "+path_phylip_corrected+" 1 i 1 "+btp+" "+modelPHYML[0]+" "+inv+" "+nbc+" "+alp+" "+" BIONJ n n"
        handle_phyml = os.popen(cmd_phyml, 'r', 1)
        for line_phyml in handle_phyml:
          print line_phyml,
        handle_phyml.close()

