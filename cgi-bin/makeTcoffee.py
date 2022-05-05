#! /usr/bin/env python

# TITULO             : Tcoffee: Alinhamento de sequencias
# AUTOR              : Kary Ocana
# DATA               : 26/10/2009
# DIFICULDADE        : 1
# ==============================================================================
# Objetivo do script: Executado do profile_phylogeny_aa.py
#                     Executa Tcoffee 
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

  os.putenv('HOME', '/var/www/.t_coffee/')
  #os.putenv('NO_ERROR_REPORT_4_TCOFFEE', '1')

  # For file in os.listdir (dirin_do_ficheiro):
  for file in os.listdir (dirin):
    if re.search ('.fasta$', file) is not None:
  
      #--- Mount directory and separate filename
      diretorio = file.split("/")
      nome = diretorio[diretorio.count('/')-1].split(".")

      #--- Mount name of fasta and mafft files
      fasta = os.path.join (dirin, file)
#      tcoffee = os.path.join (dirin, nome[0]+ ".tcoffee")
      tcoffee = os.path.join (dirin, nome[0]+ ".aln")
      treeOut = os.path.join (dirin,"tree.nj")
        
      print "Aligning: " + fasta + " ...";
      
      cmd = "t_coffee -in " + fasta + " -outfile " + tcoffee + " -output fasta_aln -newtree " + treeOut 
      handle = os.popen(cmd, 'r', 1)
      for line in handle:
        print line,
      handle.close()

