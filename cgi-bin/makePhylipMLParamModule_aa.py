#! /usr/bin/env python

#TITULO             : Phylip_ML: Parametros e sumpt parametros
#AUTOR              : Kary Soriano
#DATA               : 03/11/2009
#DIFICULDADE        : 1
# ==============================================================================
# Objetivo do script: Executado do arpa.py
# ==============================================================================
# Data da ultima alteracao do script: 	
# ==============================================================================
#-------------------------------------------------------------------------------
# declarando os modulos a usar 
#-------------------------------------------------------------------------------
import sys, os, shutil as sh
#-------------------------------------------------------------------------------
def ModulePhylipML(dirin, bootstrap):
  btp = str(bootstrap)
  
  for f in os.listdir(dirin):
    if f.endswith('_phy'):                                                    
      path_phylip_corrected = os.path.join(dirin, f)
      os.chmod(path_phylip_corrected, 0755)                                                  #Assume it's a file
      #usando o modulo paramModule_aa
      paramModulePhylipML(dirin, path_phylip_corrected, btp)
      break

def paramModulePhylipML(dirin, path_phylip_corrected, btp):
  #------------------------------------------------------------
  # Executando Parametros do ML usando PHYLIP
  #------------------------------------------------------------
  #phylipML: Maximum Likelihood: Parameter status
  #Attention: phylipML not contain consistency for evolutionary models for aa (ia Modelgenerator)

  #1.- Mudando de nome e diretorio ao outfile do Seqboot
  os.chdir(dirin)
  currentdirectory = dirin
    
  #2.- SEQBOOT
  #  Criando arquivo param_seqboot
  arq_param_s = dirin + "/param_seqboot" 
  s = file(arq_param_s, "w")
  s.write(path_phylip_corrected + '\n')
  s.write('R\n')
  s.write(btp + '\n')
  s.write('Y\n')
  s.write('431\n')
  s.close()
  
  #  Executando parametros Seqboot
  print 'Executando Seqboot...\n'
  cmd_s = "phylip seqboot < " + arq_param_s
  handle_s = os.popen(cmd_s, 'r', 1)
  for line_s in handle_s:
    print line_s,
  handle_s.close()
  
  #  Mudando de nome e diretorio ao outfile do Seqboot
  cache_location = dirin + "/outfile"
  if not (cache_location):
    os.mkdir(dirin + "/outfile")
    sh.move(dirin + "/outfile", path_phylip_corrected + "_phylipml.seqboot")
  else: 
    sh.move(dirin + "/outfile", path_phylip_corrected + "_phylipml.seqboot")
    print "exist"

  #3.- PROTML
  #  Criando arquivo param_phylipProml
  arq_param_d = dirin + "/param_phylipProml" 
  d = file(arq_param_d, "w")
  d.write(path_phylip_corrected + "_phylipml.seqboot" + '\n')
  d.write('M\n')
  d.write('D\n')
  d.write(btp + '\n')
  d.write('431\n')
  d.write('1\n')
  #JTT, PMB or PAM probability model
  d.write('Y\n')
  d.close()
  
  #  Executando parametros Protml
  print 'Executando Proml...\n'
  cmd_d = "phylip proml < " + arq_param_d
  handle_d = os.popen(cmd_d, 'r', 1)
  for line_d in handle_d:
    print line_d,
  handle_d.close()

  #  Mudando de nome e diretorio ao outfile do Protml
  cache_location3 = dirin + "/outfile"
  if not (cache_location3):
    os.mkdir(dirin + "/outfile")
    os.mkdir(dirin + "/outtree")
    sh.move(dirin + "/outfile", path_phylip_corrected + "_file_phylip.ml")
    sh.move(dirin + "/outtree", path_phylip_corrected + "_tree_phylip.ml")
  else: 
    sh.move(dirin + "/outfile", path_phylip_corrected + "_file_phylip.ml")
    sh.move(dirin + "/outtree", path_phylip_corrected + "_tree_phylip.ml")
    print "exist"

  #5.- CONSENSE
  #  Criando arquivo param_consense
  arq_param_c = dirin + "/param_consense" 
  c = file(arq_param_c, "w")
  c.write(path_phylip_corrected + "_tree_phylip.ml" + '\n')
  c.write('O\n')
  c.write('1\n')
  c.write('R\n')
  c.write('Y\n')
  c.close()
  
  print 'Executando Consense...\n'
  cmd_c = "phylip consense < " + arq_param_c
  handle_c = os.popen(cmd_c, 'r', 1)
  for line_c in handle_c:
    print line_c,
  handle_c.close()
  #Mudando de nome e diretorio ao outfile do Consense
  cache_location4 = dirin + "/outfile"
  if not (cache_location4):
    os.mkdir(dirin + "/outfile")
    os.mkdir(dirin + "/outtree")
    sh.move(dirin + "/outfile", path_phylip_corrected + "_phylipml.consenseout")
    sh.move(dirin + "/outtree", path_phylip_corrected + "_phylipml.consensetree")
  else: 
    sh.move(dirin + "/outfile", path_phylip_corrected + "_phylipml.consenseout")
    sh.move(dirin + "/outtree", path_phylip_corrected + "_phylipml.consensetree")
    print "exist"

  print 'Files param_seqboot, param_phylipProml and param_phylipML were created in: ' + dirin + "\n"  
  print 'The execution has been finished with sucess' + "\n"
  
#------------------------------------------------------------
   
