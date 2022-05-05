#! /usr/bin/env python

# TITULO            : Make Readseq 
# AUTOR             : Kary Soriano
# DATA              : 15/01/2008
# DIFICULDADE       : 1
# ==============================================================================
# Objetivo do script: Executado do myscript_nucl.py
#                     Obtencao do nexus (corrected) e phylip a partir do alinhamento 
# ==============================================================================
# (VIVAX)           : 
# (CASA)            : 
# ==============================================================================
# Data da ultima alteracao do script: 23/01/2008
# ==============================================================================
#-------------------------------------------------------------------------------
# declarando os modulos a usar 
#-------------------------------------------------------------------------------
import sys, os, re
import shutil as sh
#-------------------------------------------------------------------------------
def paramModuleReadseq(path_mafft):
  print "\tExecuting Readseq...";
  # Passando parametros para readseq - saida em formato nexus e phylip
  #   1.- Para nexus
  cmd_nexus = "readseq -all -f=17 " + path_mafft + " > " + path_mafft + "_nxs" 
  handle_nexus = os.popen(cmd_nexus, 'r', 1)
  for line_nexus in handle_nexus:
    print line_nexus,
  handle_nexus.close()
  #   2.- Para phylip
  cmd_phylip = "readseq -all -f=12 " + path_mafft + " > " + path_mafft + "_phy" 
  handle_phylip = os.popen(cmd_phylip, 'r', 1)
  for line_phylip in handle_phylip:
    print line_phylip,
  handle_phylip.close()
#-------------------------------------------------------------------------------
#readseq: last version
#java -cp readseq.jar run -all -f=17 -inform[at]=22 /home/kary/dir/d_06_casa/RT_consenso/dominios_finais/filogenia_dominios/PF00078_seed_format_LTR_nonLTR_telo_tese.aln
