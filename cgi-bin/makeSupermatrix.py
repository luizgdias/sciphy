#! /usr/bin/env python

#TITULO             : Supermatrix
#AUTOR              : Kary Soriano
#DATA               : 2011
#DIFICULDADE        : 1
# ==============================================================================
# Objetivo do script: 
# ==============================================================================
# Data da ultima alteracao do script:     
# ==============================================================================
#-------------------------------------------------------------------------------
# declarando os modulos a usar
#-------------------------------------------------------------------------------
import os, re, sys
#-------------------------------------------------------------------------------
import os, re, sys
from array import *
from Bio.Nexus import Nexus
# the combine function takes a list [(name, nexus instance)...], if we provide the
# file handles in a list we can use a list comprehension to such a list easily

def paramModule(dirin):
  file_list = os.listdir(dirin)
  handles = []
  for file in file_list:
   if re.search ('.', file) is not None:
    path = os.path.join (dirin, file)
    handles.append(open(path, 'r'))
  nexi =  [(handle.name, Nexus.Nexus(handle)) for handle in handles]

# combined.write_nexus_data(filename=out_matrix)
  combined = Nexus.combine(nexi)
  combined.export_phylip(filename='supermatrixCombined.phy')
  combined.export_fasta(filename='supermatrixCombined.fasta')

#paramModule(dirin)