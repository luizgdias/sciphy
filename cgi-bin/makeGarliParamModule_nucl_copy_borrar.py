#! /usr/bin/env python

#TITULO             : MrBayes: Parametros e sumpt parametros de MrBayes
#AUTOR              : Kary Soriano
#DATA               : 15/01/2008
#DIFICULDADE        : 1
# ==============================================================================
# Objetivo do script: Executado do myscript_nucl.py
#                     Executa Paramtros param e sumt_param do MrBayes 
# ==============================================================================
# Data da ultima alteracao do script: 	28/10/2008
# ==============================================================================
#-------------------------------------------------------------------------------
# declarando os modulos a usar 
#-------------------------------------------------------------------------------
import os, re
#-------------------------------------------------------------------------------
def paramModuleGarli(dirin, path_nexus_corrected, modelMB, paramMB):
  #------------------------------------------------------------
  # Executando Parametros do Garli 
  #------------------------------------------------------------
  #1.- GARLI: Maximum Likelihood: Parameter status
  # Trabalhando com o diretorio script onde esta o garli.conf 
  currentdirectory = os.getcwd( )
  found = False
  for conf in os.listdir(currentdirectory):
    if conf.endswith('.conf'):
      found  = True

  # Verificando o garli.conf
      arq_garli_conf = currentdirectory + "/garli.conf"
      garli_conf_in = open(arq_garli_conf,"r")
      garli_conf = garli_conf_in.read()
      garli_conf_in.close()


    
#    f = open(arq_garli_conf)
 #   o = open("output","a")
    
      string_datafname = "datafname = " + path_nexus_corrected
      print string_datafname
    #garli_conf_corrected = re.compile("(datafname = ).*")
    #garli_conf_corrected = f.replace("(datafname = ).*", string_datafname)
    #cmd_perl = os.system("perl -w makeGarliCleanModule_nucl.pl " + string_datafname)
    #cmd_w = os.system("weighbor -L 500 -b 4 -i " + path_phylip_corrected  + ".puzzledist" + " -o " + path_phylip_corrected + ".outr.wb")
  
  
    ##
    ##while 1:
    ##  line = f.readline()
    ##  if not line: break
    ##  line = line.replace(garli_conf_corrected,string_datafname)
    ##  o.write(line + "\n")
    ##  o.close()
    ##    
  ###  if re.search ('garli.conf$', conf):
  ###    found  = True
  ###    print "There is a " + conf + " file " + "in " + currentdirectory
  ###
  #### Reescrevendo arquivo garli.conf
  ###    
  ###    garli_conf_in = open(arq_garli_conf, 'a')
  ###    #if re.search('datafname = ', garli_conf) is not None:
  ###     # print "hello"
  ###    string_datafname = "datafname = " + path_nexus_corrected
  ###    garli_conf_corrected = re.compile("(datafname = ).*")
  ###    p = garli_conf_corrected.sub(string_datafname, garli_conf)        
  ###    
  ###
  ###    garli_conf_in.write (p)
  ###    garli_conf_in.close
  ###
  ###    garli_conf_in = open(arq_garli_conf, 'a')
  ###
  ###    #if re.search('ofprefix = ', garli_conf) is not None:
  ###    #  print "hello2"
  ###    string_ofprefix = "ofprefix = " + path_nexus_corrected + "_out"
  ###    garli_conf_corrected = re.compile("(ofprefix = ).*")
  ###    q = garli_conf_corrected.sub(string_ofprefix, garli_conf)        
  ###    f=open(arq_garli_conf, 'a')
  ###    f.write(q)
  ###    line = line.replace("someword","newword")
      
      #garli_conf_corrected = re.compile("(ofprefix = ).*")
      #string_ofprefix = "ofprefix = " + path_nexus_corrected + "_out"
      #p = garli_conf_corrected.sub(string_ofprefix, garli_conf)

      #L = [p, q]

      #garli_conf_corrected.sub('^datafnamei_conf.', garli_conf)
      
      #p = re.compile( '(^datafnamei*)')
      #p = re.compile( 'datafname*')
  # Dando valores aos string do garli.conf

      ##f=open(arq_garli_conf, 'w')
      #f.writelines (p)
      #f.close
  if found is False:
    print "There is not a garli.conf"
      #print p.sub( 'colour', 'blue socks and red shoes', count=1)


#.sub(replacement, string[, count=0])

#py> re.sub(r'x.*?x', repl, 'yxyyyxxyyxyy')

#>>> p = re.compile( '(blue|white|red)')
#>>> p.sub( 'colour', 'blue socks and red shoes')
#'colour socks and colour shoes'

  #Escrevendo o arquivo de saida

    
    
#>>> iterator = p.finditer('12 drummers drumming, 11 ... 10 ...')
#>>> iterator
#<callable-iterator object at 0x401833ac>
#>>> for match in iterator:
#...     print match.span()
#...
      
      #>>> p = re.compile('x*')
#>>> p.sub('-', 'abxd')
#'-a-b-d-'
      
      #reg = re.compile(^(CREATE\s+TABLE\s+CLOB)\s*(?P<sql>\w+)?;$)
      #garli_conf_corrected = garli_conf.replace('datafname.', '_')

#  text = open(path_mafft).read()
 # text_corrected = text.replace("|", "_")



  #Escrevendo o arquivo de saida
  #f=open(out_corrected, 'w')
  #f.write(text_corrected)

  ###print '  File arq_garli_conf was rewrite in: ' + dirin + "\n"

  #2.- MRBAYES: Bayesian Inference: Execution status
  #foram usados para todos os casos das execucoes de todos os scripts, a linha de comando em extenso, pode ser usado os alias fornecidos com o programa
    #1 Builds the command line with a program name and the arguments.
    #2 Runs the command and stores a handle in the handle variable. A handle for a command is the same kind of objects as a file handle: you open it (with the popen command, read from it, and close it.
    #3 Reads all the lines from the handle, and prints the joint result. 
  
  #3.- Executando parametros MrBayes
  #cmd_mb_p = "mb < " + arq_param
  #handle_p = os.popen(cmd_mb_p, 'r', 1)
  #for line_p in handle_p:
  #  print line_p,
  #handle_p.close()
 
  print 'The execution has been finished with sucess'
  
#------------------------------------------------------------
   
  ###p.write('outgroup Arabidopsis Drosophila Escherichia Synechocystis\n')

  ###p.write('mcmc ngen=10 printfreq=5 samplefreq=5 nchains=4 savebrlens=yes startingtree=random filename=' + path_nexus_corrected + '_nucl.mb.out\n') #alteracao/question script
  ###p.write('mcmc ngen=50000 printfreq=500 samplefreq=100 nchains=4 savebrlens=yes diagnfreq=10000 filename=' + path_nexus_corrected + '.nex.out\n')#question in the script
  #p.write('mcmc ngen=10 printfreq=5 samplefreq=5 nchains=4 savebrlens=yes startingtree=random filename=' + path_nexus_corrected + '.nex.out\n')#question in the script
