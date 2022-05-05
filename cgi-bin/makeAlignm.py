#! /usr/bin/env python

# TITULO             : Alignm: Alinhamento de sequencias
# AUTOR              : Kary Ocana
# DATA               : 26/10/2009
# DIFICULDADE        : 1
# ==============================================================================
# Objetivo do script: Executado do profile_phylogeny_aa.py
#                     Executa Alignm 
# ==============================================================================
# Data da ultima alteracao do script: 30/01/2008

#-------------------------------------------------------------------------------
# declarando os modulos a usar 
#-------------------------------------------------------------------------------
import os, sys, commands, re, pickle, string 
#-------------------------------------------------------------------------------
def paramModuleExecution(dirin):
# Abrindo o diretorio....
  sequence_count = '0';                                                           #contar as sequencias pro ajuste do MAFFT
  # For file in os.listdir (dirin_do_ficheiro):
  for file in os.listdir (dirin):
    if re.search ('.fasta$', file) is not None:
      #--- Mount directory and separate filename
      diretorio = file.split("/")
      nome = diretorio[diretorio.count('/')-1].split(".")

      #--- Mount name of fasta and mafft files
      fasta = os.path.join (dirin, file)
#original      alignm = os.path.join (dirin, nome[0]+ ".alignm")
      alignm = os.path.join (dirin, nome[0]+ ".aln")
      print alignm + "\n"      
      print "Aligning: " + fasta + " ...";
      
#      cmd = "/usr/local/alignm/alignM -i " + fasta + " -o " + alignm + " -otype fasta"
      cmd = "/usr/bin/align_m -i " + fasta + " -o " + alignm + " -otype fasta"
      print cmd
      handle = os.popen(cmd, 'r', 1)
      for line in handle:
        print line,
      handle.close()


