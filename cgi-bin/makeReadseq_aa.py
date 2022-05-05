#! /usr/bin/env python

# TITULO            : Make Readseq 
# AUTOR             : Kary Soriano
# DATA              : 15/01/2008
# DIFICULDADE       : 1
# ==============================================================================
# Objetivo do script: Executado do profile_phylogeny_aa.py
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

import os, sys, commands, re, shutil as sh, optparse, time, datetime
import sys, random, string, subprocess, json
import getopt
# import psutil
from optparse import OptionParser


# from dfa_lib_python.dataflow import Dataflow
# from dfa_lib_python.transformation import Transformation
# from dfa_lib_python.attribute import Attribute
# from dfa_lib_python.attribute_type import AttributeType
# from dfa_lib_python.set import Set
# from dfa_lib_python.set_type import SetType
# from dfa_lib_python.task import Task
# from dfa_lib_python.dataset import DataSet
# from dfa_lib_python.element import Element
# from dfa_lib_python.epoch import Epoch
# from dfa_lib_python.telemetry import Telemetry
# from dfa_lib_python.telemetry_cpu import TelemetryCPU 
#-------------------------------------------------------------------------------
def paramModuleReadseq(path_mafft):
  print "\tExecuting Readseq...";
  print path_mafft
  # Passando parametros para readseq - saida em formato nexus e phylip
  #   1.- Para nexus
  cmd_nexus = "readseq -all -f=17 " + path_mafft + " > " + path_mafft + "_nxs" 
  print "COMECOU READSEQ"
  handle_nexus = os.popen(cmd_nexus, 'r', 1)
  for line_nexus in handle_nexus:
    print line_nexus,
  handle_nexus.close()
  print "TERMINOU READSEQ"
  #   2.- Para phylip
  cmd_phylip = "readseq -all -f=12 " + path_mafft + " > " + path_mafft + "_phy" 
  handle_phylip = os.popen(cmd_phylip, 'r', 1)
  for line_phylip in handle_phylip:
    print line_phylip,
  handle_phylip.close()


#-------------------------------------------------------------------------------
#readseq: last version
#java -cp readseq.jar run -all -f=17 -inform[at]=22 /home/kary/dir/d_06_casa/RT_consenso/dominios_finais/filogenia_dominios/PF00078_seed_format_LTR_nonLTR_telo_tese.aln
