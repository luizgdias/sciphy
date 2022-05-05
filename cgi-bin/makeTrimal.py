#! /usr/bin/env python

# TITULO             : Trimal: Curacao de sequencias
# AUTOR              : Kary Ocana
# DATA               : 13/11/2009
# DIFICULDADE        : 1
# ==============================================================================
# Objetivo do script: Executado do arpa_lc.py
#                     Executa trimal 
# ==============================================================================
# Data da ultima alteracao do script: 
#-------------------------------------------------------------------------------
# declarando os modulos a usar 
#-------------------------------------------------------------------------------
import os, sys, commands, re, pickle, string 
#-------------------------------------------------------------------------------
def paramModuleExecution(path_alignment):
# Abrindo o diretorio....
  # Passando parametros para trimal (alinhamento)
  #cmd_trimal = "trimal -in  " + path_alignment + " -out " + path_alignment + ".trimal -gt 0.9 -cons 60"
  cmd_trimal = "trimal -in  " + path_alignment + " -out " + path_alignment + " -gt 0.9 -cons 60"
  handle_trimal = os.popen(cmd_trimal, 'r', 1)
  for line_trimal in handle_trimal:
    print line_trimal,
  handle_trimal.close()

