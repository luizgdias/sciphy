#! /usr/bin/env python

# TITULO            : Remove pipe 
# AUTOR             : Kary Soriano
# DATA              : 15/01/2008
# DIFICULDADE       : 1
# ==============================================================================
# Objetivo do script: Executado do myscript_nucl.py
#                     Substitui pipes | por _ de alinhamentos (logo nexus), usado por MrBayes. 
# ==============================================================================
# (VIVAX)           : python remove_pipe_nucl.py /disk1/home/kary/d_06/projeto/script/script_nucl_pipeline/python/fasta/rh/rh.mafft
# (CASA)            : python remove_pipe_nucl.py /home/kary/dir/d_06_casa/script/script_nucl_pipeline/python/fasta/rh/rh.mafft
# ==============================================================================
# Data da ultima alteracao do script: 15/01/2008
# ==============================================================================
#-------------------------------------------------------------------------------
# declarando os modulos a usar 
#-------------------------------------------------------------------------------
import sys, os
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
('\t', '_'),
]

def paramModule(path_mafft):
   print "2 Correcting and removing pipes: replaces all findStr by repStr in file: " + path_mafft + "...\n"
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






