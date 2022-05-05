#! /usr/bin/env python

# TITULO            : Remove pipe 
# AUTOR             : Kary Soriano
# DATA              : 15/01/2008
# DIFICULDADE       : 1
# ==============================================================================
# Objetivo do script: Executado do profile_phylogeny_aa.py
#                     Substitui pipes | por _ de alinhamentos (logo nexus), usado por MrBayes. 
# ==============================================================================
# (VIVAX)           : python remove_pipe_aa.py /disk1/home/kary/d_06/projeto/script/script_aa_pipeline/python/fasta/rh/rh.mafft
# (CASA)            : python remove_pipe_aa.py /home/kary/dir/d_06_casa/script/script_aa_pipeline/python/fasta/rh/rh.mafft
# ==============================================================================
# Data da ultima alteracao do script: 15/01/2008
# ==============================================================================
#-------------------------------------------------------------------------------
# declarando os modulos a usar 
#-------------------------------------------------------------------------------
import sys, os, re

#-------------------------------------------------------------------------------
findreplace = [
('|' , '_'),
('(' , '_'),
(')' , '_'),
(';' , '_'),
(',' , '_'),
('/' , '_'),
('\\' , '_'),
('[' , '_'),
(']' , '_'),
(' ', '_'),
(':', '_'),
('-', '_'),
('*', '_'),
('.', '_'),
('\t', '_'),
]

#def paramModule(path_mafft):
def paramModule(dirin):
  print "DIRIN:**************** "+ dirin
  # For file in os.listdir (dirin_do_ficheiro):
  for file in os.listdir (dirin):
    if re.search ('filein.fasta', file) is not None:
      diretorio = file.split("/")
      nome = diretorio[diretorio.count('/')-1].split(".")
      #--- Mount name of fasta and mafft files
      path_mafft = os.path.join (dirin, file)
      print "***PATH MAFFT: "+ path_mafft
      #os.chmod(path_mafft, 0777)  # Assume it's a file
      #mafft = os.path.join (dirin, nome[0]+ ".mafft")
      
      print "\tCleaning and removing pipes in file: " + path_mafft + "..."
      tempName=path_mafft+'~~~'
      input = open(path_mafft)
      output = open(tempName,'w')
      s=input.read()
      for couple in findreplace:
          outtext=s.replace(couple[0],couple[1])
          s=outtext
      output.write(outtext)
      output.close()
      input.close()
      os.rename(tempName,path_mafft) 