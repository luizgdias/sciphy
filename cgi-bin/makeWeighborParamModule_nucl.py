#! /usr/bin/env python

#TITULO             : Weighbor: Parametros e sumpt parametros
#AUTOR              : Kary Soriano
#DATA               : 31/01/2008
#DIFICULDADE        : 1
# ==============================================================================
# Objetivo do script: Executado do myscript_nucl.py
#                     Executa Parametros do Weighbor
# ==============================================================================
# Data da ultima alteracao do script: 	31/01/2008
#					//2008
# ==============================================================================
#-------------------------------------------------------------------------------
# declarando os modulos a usar 
#-------------------------------------------------------------------------------
import sys, os, shutil as sh
#-------------------------------------------------------------------------------
def paramModuleWeighbor(dirin, path_phylip_corrected, modelWB, bootstrap, nb_categ):
  btp = str(bootstrap)
  mod = str(modelWB)
  nbc = str(nb_categ)

  #Mudando de nome e diretorio ao outfile do Seqboot
  os.chdir(dirin)
  currentdirectory = dirin

  #1.- WEIGHBOR: Parameter status
  # Criando arquivo param_seqboot
  arq_param_s = dirin + "/param_seqboot" 
  s = file(arq_param_s, "w")
  s.write(path_phylip_corrected + '\n')
  s.write('R\n')
  s.write(btp + '\n')
  s.write('Y\n')
  s.write('431\n')
  s.close()

  # Criando arquivo param_puzzle 
  arq_param_p = dirin + "/puzzle.cmds" 
  p = file(arq_param_p, "w")
  p.write('k\n')
  p.write('k\n')
  p.write('k\n')
  p.write(mod + '\n')
  p.write('w\n')
  p.write('c\n')
  p.write(nbc + '\n')
  p.write('y\n')
  p.close()
  
  print 'Files param_seqboot and puzzle.cmds were created in: ' + dirin

  #2.- WEIGHBOR: Execution status
  #foram usados para todos os casos das execucoes de todos os scripts, a linha de comando em extenso, pode ser usado os alias fornecidos com o programa
    #1 Builds the command line with a program name and the arguments.
    #2 Runs the command and stores a handle in the handle variable. A handle for a command is the same kind of objects as a file handle: you open it (with the popen command, read from it, and close it.
    #3 Reads all the lines from the handle, and prints the joint result. 
  
  #3.- Executando parametros Seqboot
  print 'Executando Seqboot...\n'
  cmd_s = "phylip seqboot < " + arq_param_s                                     #ver em que casos se usa phylip (no em fedora)
  handle_s = os.popen(cmd_s, 'r', 1)
  for line_s in handle_s:
    print line_s,
  handle_s.close()
  
  #Mudando de nome e diretorio ao outfile do Seqboot
  #currentdirectory = os.getcwd( )
  #currentdirectory = dirin
  sh.move(currentdirectory + "/outfile", path_phylip_corrected + ".seqboot")

  #4.- Calculando L do InvariantAwkWeighbor
  print 'Calculating L: Opening the _phy file for read'
  # Extraindo o comprimento total do alinhamento do arquivo _phy
  text_phy = open(path_phylip_corrected).read()
  first_line_lenght = text_phy.split("\n")
  first_line_lenght_clean = first_line_lenght.pop(0)
  first_line_lenght_clean = first_line_lenght_clean.split(" ")
  first_line_lenght_clean = first_line_lenght_clean.pop(2)
  # 4.1 Calculando o invariantAwk (awk, numero de caracteres em cada coluna, tail mostra 2 cifras)
  cmd_iawk = os.system("tail -n +2 " + path_phylip_corrected + " | awk -f /var/www/arpa/cgi-bin/invariant.awk")   # para fedora 5 e Ubuntu
  # 4.2 Calculando "the number of varying sites" 
  L = int(first_line_lenght_clean) - (int(cmd_iawk)*int (first_line_lenght_clean))
  L = int(L)
  Llast = str(L)
  Llast.strip()
  print Llast
  
  #5.- Executando parametros Puzzleboot
  print 'Executando Puzzleboot...\n'
  # 5.1 Create weighbor directory in the directory
  dirname = "weighbor"
  os.mkdir(dirname)
  # 5.2Copy the need files to the weighbor directory
  sh.copy2(path_phylip_corrected + '.seqboot', dirname)
  sh.copy2('puzzle.cmds', dirname)
  # 5.3 Read the files in the new weighbor directory
  found = False
  for f in os.listdir(dirname):
    if f.endswith('.seqboot'):
      found  = True
      path_phylip_correctedW = os.path.join("./" + dirname, f)
      os.chmod(path_phylip_correctedW, 0755)                                      #Assume it's a file
      print "4", currentdirectory
      print "5", path_phylip_correctedW
      #5.4 Execute puzzleboot in the new weighbor directory
      cmd_p = "puzzleboot.sh " + path_phylip_correctedW
      handle_p = os.popen(cmd_p, 'r', 1)
      for line_p in handle_p:
        print line_p,
      handle_p.close()
  if found is False:
    print "There is not .seqboot.file"
    sys.exit(2)

  #6.- Executando parametros Weighbor
  print 'Executando Weighbor...\n'
  cmd_w = "weighbor -L " + Llast + " -b 4 -i " + path_phylip_correctedW + ".outdist -o " + path_phylip_correctedW + ".outr.wb"
  handle_w = os.popen(cmd_w, 'r', 1)
  for line_w in handle_w:
    print line_w,
  handle_w.close()
  print 'Weighbor executado...\n'

  #7.- Executando parametros Consense
  # Criando arquivo param_consense
  arq_param_c = dirname + "/param_consense" 
  c = file(arq_param_c, "w")
  c.write(path_phylip_correctedW + '.outr.wb\n')
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
  sh.move("outfile", path_phylip_correctedW + ".consenseout")
  sh.move("outtree", path_phylip_correctedW + ".consensetree")
    
  print 'The execution has been finished with sucess'
  
#------------------------------------------------------------
   
