#! /usr/bin/env python

# TITULO             : PAUP Neighbor-Joining: Construcao de Arvores filogeneticas por NJ usando PAUP
# AUTOR              : Kary Soriano
# DATA               : 21/01/2008
# DIFICULDADE        : 1

# ==============================================================================
# Objetivo do script: Executado do profile_phylogeny_aa.py
#                     Executar PAUP para NJ
# (VIVAX)           : python makePaupNJ_pipeline_aa.py /disk1/home/kary/d_06/projeto/script/script_aa_pipeline/python/fasta/rh blosum
# ==============================================================================
# Data da ultima alteracao do script: 	24/01/2008
#					21/01/2008
# ==============================================================================
#-------------------------------------------------------------------------------
# declarando os modulos a usar 
#-------------------------------------------------------------------------------
import sys, os
#-------------------------------------------------------------------------------
#Abrindo o diretorio 
#dirin = sys.argv[1]
#dirin_arg_pas = sys.argv[1:]
#modelMG = sys.argv[2]
#modelMG_arg_pas = sys.argv[2:]
#print "O nome do diretorio de entrada e o modelMG sao: " + dirin + modelMG
#print "E os argumentos passados sao: " + str(dirin_arg_pas)

def ModulePaupNJ(dirin, path_mafft):
  for f in os.listdir(dirin):
    if f.endswith('_nxs'):                                                    
      path_nexus_corrected = os.path.join(dirin, f)
      os.chmod(path_mafft, 0755)                                                  #Assume it's a file
      #nexus_corrected = f
  
      #usando o modulo paramModule_aa
      import makePaupNJParamModule_aa 
      makePaupNJParamModule_aa.paramModulePaupNJ(dirin, path_nexus_corrected)
      break
  #print f									#arquivo fasta fora do loop, corrected dentro do loop
  #print nexus_corrected								#arquivo corrected fora do loop
  #print path_mafft								#dirin + arquivo nexus_corrected

