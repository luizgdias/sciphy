#! /usr/bin/env python

#TITULO             : RAxML: Parametros para a execucao de RAxML
#AUTOR              : Kary Soriano
#DATA               : 03/11/2008
#DIFICULDADE        : 1
# ==============================================================================
# Objetivo do script: Executado do myscript_aa.py
#                     Executa Parametros 
# ==============================================================================
# Data da ultima alteracao do script: 	03/11/2008
# ==============================================================================
#-------------------------------------------------------------------------------
# declarando os modulos a usar 
#-------------------------------------------------------------------------------
import os, re
#-------------------------------------------------------------------------------
def paramModuleRaxml(dirin, model, rates_raxml_aa, freq_raxml_aa, bootstrap, nb_categ,):
  btp = str(bootstrap)
  mod = str(model)
  nbc = str(nb_categ)
  rat = str(rates_raxml_aa)
  fre = str(freq_raxml_aa)
  model = rat + mod + fre
  print nbc
  print model
  
  #------------------------------------------------------------
  # Executando Parametros do Raxml 
  #------------------------------------------------------------
  #1.- RAXML: Maximum Likelihood: Parameter status
  # Trabalhando com o diretorio script onde esta o raxml.conf 
  for f in os.listdir(dirin):
    if f.endswith('_phy'):                                                    
      phylip = f
      print "Executing RAxML:\n"
      print dirin
  #2.- RAXML: Estimating a Single Maximum-Likelihood Tree from Protein Sequences
      os.chdir(dirin)
      cmd_raxml_s = "raxmlHPC -s " + phylip + " -n " + phylip + "_raxml_tree1.singleTree -c " + nbc + " -f d -m " + model + " -p 12345"# + " -o " + ">SceRH"
      handle_s = os.popen(cmd_raxml_s, 'r', 1)
      for line_s in handle_s:
        print line_s,
      handle_s.close()
  #3.- RAXML: Estimating a Set of Non-Parametric Bootstrap Trees
      ###os.chdir(dirin)
      #cmd_raxml_b = "raxmlHPC -s " + phylip + " -n " + phylip + ".raxml -c 4 -f d -m " + modelMB + " -o " + ">SceRH -b 234534251 -N 100"
      cmd_raxml_b = "raxmlHPC -s " + phylip + " -n " + phylip + "_tree2.raxml -c " + nbc + " -f d -m " + model + " -b 234534251 -N " + btp + " -p 12345"
      handle_b = os.popen(cmd_raxml_b, 'r', 1)
      for line_b in handle_b:
        print line_b,
      handle_b.close()
  #4.- RAXML: Projecting Bootstrap Confidence Values onto ML Tree
      ###os.chdir(dirin)
      #cmd_mb_p = "ls -lh" 
      cmd_raxml_c = "raxmlHPC -f b -m " + model + " -c " + nbc + " -s " + phylip + " -z " + "RAxML_bootstrap." + phylip + "_tree2.raxml -t RAxML_bestTree." + phylip + "_raxml_tree1.singleTree -n " + phylip + "_tree3.BS_TREE"
      handle_c = os.popen(cmd_raxml_c, 'r', 1)
      for line_c in handle_c:
        print line_c,
      handle_c.close()
  
print 'The execution has been finished with sucess'

  # print 'ARVORE: \n'
  # raxmltree = open("RAxML_bestTree.file.aln_phy_raxml_tree1.singleTree", "r")
  # raxmltree   = raxmltree.readlines()
  # print raxmltree
  
#------------------------------------------------------------
#exemplos: 
#Mudar Para: (http://www.embl-heidelberg.de/~seqanal/courses/commonCourseContent/usingRaxml.html)
#nohup raxmlHPC -s gag_aa_protozoario_edit_root.mafft_phy -n gag.raxml.singleTree -c 4 -f d -m PROTMIXIBLOSUM62F -o SceGAGPOL_ &
#nohup raxmlHPC -s gag_aa_protozoario_edit_root.mafft_phy -n gag.raxml -c 4 -f d -m PROTMIXIBLOSUM62F -o SceGAGPOL_ -b 234534251 -N 100 &


###
#nohup raxmlHPC -f b -m PROTMIXIBLOSUM62F -c 4 -s gag_aa_protozoario_edit_root.mafft_phy -z RAxML_bootstrap.gag.raxml -t gag.raxml.singleTree -n BS_TREE
#Este e para raxml 7.2.1 ###raxmlHPC -f b -m PROTCATWAG -c 4 -s rh.mafft_phy -z RAxML_bootstrap.rh.mafft_phy.raxml -t RAxML_bestTree.rh.mafft_phy_raxml.singleTree -n rh.mafft_phy.BS_TREE
###


#raxmlHPC -f a -s alg -x 12345 -# 100 -m GTRCAT -n TEST.
#SERIA:    raxmlHPC -f a -s gagAAR.mafft_phy -x 12345 -# 100 -m PROTMIXIBLOSUM62F -o SceGAGPOL -n gagAAR.raxml-out
#raxmlHPC -s aqp1RootSM.mafft_phy -n aqp1RootSM_raxml-out -m PROTGAMMAWAGF -o >OUT -b 123476 -# 100
#raxmlHPC -k -s rh_aa.mafft_phy -n rh_aa_phy_raxml-out -m GTRCAT -o gi_6812406 -b 123476 -# 100
#1.- Alignment Error Checking
#In case that RAxML detects Identical Sequences and/or Undetermined Columns and was executed,
#e.g., with -n alignmentName it will automatically write an alignment file called alignmentName.reduced
#with Identical Sequences and/or Undetermined Columns removed. If this is detected for a multiple model
#analysis a respective model file modelFileName.reduced will also be written. In case RAxML encounters
#identical sequence names or undetermined sequences or illegal characters in taxon names it will exit with
#an error and you will have to fix your alignment.
#2.-      Program Options
#raxmlHPC[-MPI|-PTHREADS] -s sequenceFileName
#                         -n outputFileName
#                         -m substitutionModel
#                         [-a weightFileName]
#                         [-b bootstrapRandomNumberSeed]
#                         [-c numberOfCategories]
#                         [-d]
#                         [-e likelihoodEpsilon]
#                         [-E excludeFileName]
#                         [-f a|b|c|d|e|g|h|i|j|m|n|o|p|s|t|w|x]
#                         [-g groupingFileName]
#                         [-h]
#                         [-i initialRearrangementSetting]
#                                             6
#[-j]
#[-k]
#[-l sequenceSimilarityThreshold]
#[-L sequenceSimilarityThreshold]
#[-M]
#[-o outGroupName1[,outGroupName2[,...]]]
#[-p parsimonyRandomSeed]
#[-P proteinModel]
#[-q multipleModelFileName]
#[-r binaryConstraintTree]
#[-t userStartingTree]
#[-T numberOfThreads]
#[-u multiBootstrapSearches]
#[-v]
#[-w workingDirectory]
#[-x rapidBootstrapRandomNumberSeed]
#[-y]
#[-z multipleTreesFile]
##[-#|-N numberOfRuns]

#3.-       -# numberOfRuns
#Specifies the number of alternative runs on distinct starting trees. E.g. if
#-# 10 is specified RAxML will compute 10 distinct ML trees starting from
#10 distinct randomized maximum parsimony starting trees. In combination
#with the -b option, this will invoke a multiple bootstrap analysis

#4.-   -o outgroupName(s)
#Specify the name/names of the outgroup taxa, e.g.,-o Mouse or -o Mouse,Rat. Dont leave spaces between
#the taxon names in the list! If there is more than one outgroup a check for monophyly will be performed. If
#the outgroups are not monophyletic the tree will be rooted at the first outgroup in the list and a respective
#warning will be printed.
#Example: raxmlHPC -s alg -m GTRGAMMA -o Rat,Mouse -n TEST

