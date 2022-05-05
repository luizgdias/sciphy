#! /usr/bin/env python

# TITULO             : Trimal: Curacao de sequencias
# AUTOR              : Kary Ocana
# DATA               : 13/11/2009
# DIFICULDADE        : 1
# ==============================================================================
# Objetivo do script: Executado do arpa_lc.py
#                     Executa gblocks 
# ==============================================================================
# Data da ultima alteracao do script: 
#-------------------------------------------------------------------------------
# declarando os modulos a usar 
#-------------------------------------------------------------------------------
import os, sys, commands, re, pickle, string, shutil as sh 
#-------------------------------------------------------------------------------
def paramModuleExecution(path_alignment):
# Abrindo o diretorio....
  # Passando parametros para gblocks (alinhamento)
  cmd_gblocks = "Gblocks " + path_alignment + " -e=-gb1 -b4=6"
  handle_gblocks = os.popen(cmd_gblocks, 'r', 1)
  for line_gblocks in handle_gblocks:
    print line_gblocks,
  handle_gblocks.close()
  
  #mudar terminacao -gb1 para aln
  sh.copy(path_alignment+'-gb1',path_alignment)




