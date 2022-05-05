#!/usr/bin/python

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

def ModulePhyml(dirin, param_model_evol):
  for f in os.listdir(dirin):
    if f.endswith('_phy'):                                                    
      path_phylip_corrected = os.path.join(dirin, f)
      os.chmod(path_phylip_corrected, 0755)                                     # Assume it's a file
  #print "este dirin para PHYML" + dirin 								#arquivo fasta fora do loop, corrected dentro do loop
  #print nexus_corrected							# arquivo corrected fora do loop
  #print path_phylip_corrected							# dirin + arquivo nexus_corrected
  #print "este modelo para Phyml" + param_model_evol + f

  #Phyml Parameters: Comparing and searching Modelgenerator evolutionary models 
  #Attention: Phyml and Modelgenerator have different evolutionary models 
  modelPHYML = ['JTT','MtREV','WAG','DCMut','RtREV','CpREV','VT','Blosum62','MtMam','Dayhoff']
    #Verificando se o modelo evolutivo eleito e um dos parametros do Phyml
    #Pertencem a MG (param_model_evol): BLOSUM62 CPREV Dayhoff JTT MTREV24  VT WAG DCMut RtREV MtMam
    #Pertencem a PHYML: modelPHYML, "This parameter sets the rate matrix for amino acid data"
  found = False
  for x in modelPHYML[:]:                                                       # make a slice copy of the entire list
    m = re.match(param_model_evol[0] + "$", x, re.IGNORECASE)                      # Usando so se o modelMG e identico com versao! do contrario usar #m = re.match(modelMG + "*", x, re.IGNORECASE)
    if m:
      
      #1.- PHYML: Se o modelo PHYML bate com MG
      found  = True
      modelHit = repr(x).split("'");
      print "param_model_evol => ", param_model_evol, ", modelPHYML => ", modelHit[1]   #print "modelPHYML => ", repr(x), ", modelMG => ", repr(m.group(0))
      print "Executing Phyml using modelMG - ModelPHYML =>", modelHit[1],"\n\n";
      #usando o modulo paramModule do Phyml
      #cmd_phyml = "phyml " + path_phylip_corrected + " 1 i 1 10 " + modelHit[1] + " 0.0 4 1.0 BIONJ n n"
      cmd_phyml = "phyml_linux " + path_phylip_corrected + " 1 i 1 100 " + modelHit[1] + " 0.0 4 1.0 BIONJ n n"
      #casa
      #cmd_phyml = "phyml " + path_phylip_corrected + " 1 i 1 100 " + modelHit[1] + " 0.0 4 1.0 BIONJ n n"
      handle_phyml = os.popen(cmd_phyml, 'r', 1)
      for line_phyml in handle_phyml:
        print line_phyml,
      handle_phyml.close()
      
      #2.- PHYML: Se o modelo PHYML nao bate com MG, usando o modelo poisson default de PHYML
  if found is False:
    print "modelMG => ", modelMG, ", modelPHYML => ", "No hit"
    print "No found evolutionary modelMG consistent in ModelPHYML"
    print "Executing Phyml using default modelPHYML =>", modelPHYML[0], "\n\n";
    #usando o modulo paramModule
    #cmd_phyml = "phyml " + path_phylip_corrected + " 1 i 1 10 " + modelPHYML[0] + " 0.0 4 1.0 BIONJ n n"
    cmd_phyml = "phyml_linux " + path_phylip_corrected + " 1 i 1 100 " + modelPHYML[0] + " 0.0 4 1.0 BIONJ n n"
    #casa
    ###cmd_phyml = "phyml " + path_phylip_corrected + " 1 i 1 100 " + modelPHYML[0] + " 0.0 4 1.0 BIONJ n n"
    handle_phyml = os.popen(cmd_phyml, 'r', 1)
    for line_phyml in handle_phyml:
      print line_phyml,
    handle_phyml.close()





#phyml [ sequences data_type format data_sets bootstrap_sets model
#      [kappa] invar nb_categ alpha tree opt_topology opt_lengths ]
#AA sequences :    ./phyml seqs2 1 i 1 5 JTT 0.0 4 1.0 BIONJ n n

#ARQUIVOS DE SAIDA DO PHYML
#-rw-rw-r-- 1 kary kary  427 Jul 24 09:38 rh.mafft.phylip_phyml_boot_stats.txt
#-rw-rw-r-- 1 kary kary  125 Jul 24 09:38 rh.mafft.phylip_phyml_boot_trees.txt
#-rw-rw-r-- 1 kary kary   13 Jul 24 09:38 rh.mafft.phylip_phyml_lk.txt
#-rw-rw-r-- 1 kary kary  381 Jul 24 09:38 rh.mafft.phylip_phyml_stat.txt
#-rw-rw-r-- 1 kary kary  127 Jul 24 09:38 rh.mafft.phylip_phyml_tree.txt

#PHYML enables to analyze one or several data sets in conjunction with one or several starting trees.
# PHYML produces several results files : <sequence file name>_phyml_lk.txt : likelihood value(s)
# <sequence file name>_phyml_tree.txt : inferred tree(s)
# <sequence file name>_phyml_stat.txt : detailed execution stats
# <sequence file name>_phyml_boot_trees.txt : bootstrap trees (special case)
# <sequence file name>_phyml_boot_stats.txt : bootstrap statistics (special case)  

#PAGES
#http://bioweb.pasteur.fr/seqanal/tmp/phyml/A48324311852822/
#http://atgc.lirmm.fr/phyml/usersguide_cmdline.html

#        Examples
#        DNA sequences :   ./phyml seqs1 0 i 2 0 HKY 4.0 e 1 1.0 BIONJ y n
#        AA sequences :    ./phyml seqs2 1 i 1 5 JTT 0.0 4 1.0 BIONJ n n

 
 
 
 
 #para DNA
 
 #HKY
 #F84
 #TN93
 #GTR
 #custom
 #JC69
 #K2P
 #F81
 
 
