#! /usr/bin/env python

# TITULO             : Mafft: Alinhamento de sequencias
# AUTOR              : Kary Soriano
# DATA               : 11/01/2008
# DIFICULDADE        : 1
# ==============================================================================
# Objetivo do script: Executado do myscript_nucl.py
#                     Executa Mafft 
# ==============================================================================
# Data da ultima alteracao do script: 30/01/2008
#                                   : 15/01/2008
# ==============================================================================
#-------------------------------------------------------------------------------
# declarando os modulos a usar 
#-------------------------------------------------------------------------------
import os, sys, commands, re, pickle, string 
#-------------------------------------------------------------------------------
#dirin_do_ficheiro = sys.argv[0]
#dirin_arg_pas = sys.argv[0:]
###print "O nome do diretorio de entrada do ficheiro e: " + dirin_do_ficheiro 
###print "E os argumentos passados sao: " + str(dirin_arg_pas)

def paramModuleExecution(dirin):
# Abrindo o diretorio....
  sequence_count = '0';                                                           #contar as sequencias pro ajuste do MAFFT
  # For file in os.listdir (dirin_do_ficheiro):
  for file in os.listdir (dirin):
    if re.search ('filein.fasta$', file) is not None:
      #--- Mount directory and separate filename
      diretorio = file.split("/")
      nome = diretorio[diretorio.count('/')-1].split(".")

      #--- Mount name of fasta and mafft files
      fasta = os.path.join (dirin, file)
      mafft = os.path.join (dirin, nome[0]+ ".aln")
      
      print "Aligning: " + fasta + " ...";
      
      # Lendo o arquivo e contando o numero de sequencias para usar a melhor opcao oferecida pelo MAFFT 
      text = open(fasta).read()
      sequence_count = string.count(text, '>')
      
      # Criar um alinhamento com mafft dependendo do numero de seqs, buscando maior precisao e eficiencia
      if sequence_count < 200:
        print "\tCreating a multiple alignment for " + fasta + " using MAFFT (L-INS-i < 200 seqs)...";
        # Foram usados para todos os casos, a linha de comando em extenso, pode ser usado os alias fornecidos com o programa
          #1 Builds the command line with a program name and the arguments.
          #2 Runs the command and stores a handle in the handle variable. A handle for a command is the same kind of objects as a file handle: you open it (with the popen command, read from it, and close it.
          #3 Reads all the lines from the handle, and prints the joint result. 
        cmd = "mafft --quiet --localpair --maxiterate 1000 " + fasta + " > " + mafft 
        handle = os.popen(cmd, 'r', 1)
        for line in handle:
          print line,
        handle.close()
        
        #Limpando o contador
        sequence_count = '0';
      elif sequence_count > 2000:
        print "\tCreating a multiple alignment for " + fasta + " using MAFFT (FFT-NS-1 > 2000 seqs)...";
        cmd = "mafft --quiet --retree 1 --maxiterate 0 " + fasta + " > " + mafft 
        handle = os.popen(cmd, 'r', 1)
        for line in handle:
          print line,
        handle.close()      
        sequence_count = '0';
      else:
        print "\tCreating a multiple alignment for " + fasta + " using MAFFT (FFT-NS-i)...";      
        cmd = "mafft --quiet --retree 2 --maxiterate 1000 " + fasta + " > " + mafft 
        handle = os.popen(cmd, 'r', 1)
        for line in handle:
          print line,
        handle.close()    
        sequence_count = '0';







