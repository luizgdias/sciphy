
# -*- coding: utf-8 -*-
#! /usr/bin/env python

# TITULO            : ARPA pipeline
# AUTOR             : Kary Ocana
# DATA              : 22/10/2009
# DIFICULDADE       : 1
# ==============================================================================
# Objetivo do script: Rodado como o programa principal. Executar Mafft, Readseq,
#                     remove_pipe, Modelgenerator, modulos/script e algoritmos de filogenia 
# Usar o argumento  : Ver usage
# ==============================================================================
# Data da ultima alteracao do script: 01/07/2009
# ==============================================================================
#--------------------------------------------------------------------------------
# declarando os modulos a usar 
#-------------------------------------------------------------------------------
import os, sys, commands, re, shutil as sh, optparse, time, datetime, threading
import sys, random, string, psutil, subprocess, json
import getopt
from optparse import OptionParser

from telemetry_functions import Telemetria
from dfa_lib_python.dataflow import Dataflow
from dfa_lib_python.dependency import Dependency
from dfa_lib_python.transformation import Transformation
from dfa_lib_python.attribute import Attribute
from dfa_lib_python.attribute_type import AttributeType
from dfa_lib_python.set import Set
from dfa_lib_python.set_type import SetType
from dfa_lib_python.task import Task
from dfa_lib_python.dataset import DataSet
from dfa_lib_python.element import Element
from dfa_lib_python.epoch import Epoch
from dfa_lib_python.telemetry import Telemetry
from dfa_lib_python.telemetry_cpu import TelemetryCPU
from dfa_lib_python.telemetry_memory import TelemetryMemory
from dfa_lib_python.telemetry_disk import TelemetryDisk 

def validate_parametersA(alignment):
  alignmentAllDefault = ['alignm','clustalw','lobster','mafft','muscle','probcons','tcoffee']  
  if (esta_em_alignmentAllDefault(alignment, alignmentAllDefault)):
    return 1
  else:
    print "The alignment is unrecognizable"
    sys.exit(2)

def esta_em_alignmentAllDefault(alignment, alignmentAllDefault):
  for a in alignmentAllDefault:
    if alignment.lower() == a.lower():
      print 'Alignment found: ' + a 
      return 1
  return 0

def validate_parametersT(trimmer):
  trimmerAllDefault = ['total','gblocks','trimal']  
  if (esta_em_trimmerAllDefault(trimmer, trimmerAllDefault)):
    return 1
  else:
    print "The trimmer is unrecognizable"
    sys.exit(2)

def esta_em_trimmerAllDefault(trimmer, trimmerAllDefault):
  for t in trimmerAllDefault:
    if trimmer.lower() == t.lower():
      print 'Trimmer found: ' + str(t)
      return 1
  return 0

def validate_parameters(program):
  programAllDefault = ['garli','mrbayes','paup_nj','paup_mp','paup_ml','phylip_nj','phylip_mp','phylip_ml','phyml','raxml','weighbor','algorithms_aa_1','algorithms_aa_2','algorithms_aa_3']  
  if (esta_em_programAllDefault(program, programAllDefault)):
    return 1
  else:
    print "The program is unrecognizable"
    sys.exit(2)

def esta_em_programAllDefault(program, programAllDefault):
  for p in programAllDefault:
    if program.lower() == p.lower():
      print 'Program found: ' + p 
      return 1
  return 0

def alphabet_nucl(filename):
  file = open(filename)
  for line in file.readlines():
    if line[0] != '>':
      tam = len (line)
      for i in range(tam):
        if line[i].upper() != 'A' and line[i].upper() != 'T' and line[i].upper() != 'C' and line[i].upper() != 'G':
          if line [i] == '\n': break
          print "It is not nucleotide." 
          return 0
        else:
          print "Data_type found: nucl (nucleotide)"
          return 1
  file.close()

def alphabet_aa (filename):
  file = open(filename)
  for line in file.readlines():
    if line[0] != '>':
      tam = len (line)
      for i in range(tam):
        if line [i] != 'A' and line [i] != 'B' and line [i] != 'C' and line [i] != 'D' and  line [i] != 'E' and line [i] != 'F' and line [i] != 'G' and line [i] != 'H' and line [i] != 'I' and line [i] != 'K'and  line [i] != 'L' and line [i] != 'M' and line [i] != 'N' and  line [i] != 'P' and line [i] != 'Q' and line [i] != 'R' and  line [i] != 'S' and line [i] != 'T' and line [i] != 'U' and  line [i] != 'V' and line [i] != 'W' and line [i] != 'X' and line [i] != 'Y' and line [i] != 'Z':
          if line [i] == '\n': break
          print "It is not amino acid" 
          return 0
        else:
          print "Data_type found: aa (amino acid)"
          return 1
  file.close()

def modelgenerator_nucl(model): #mudar para nucl
  modelAllDefault = ['F84','JC','F81','HKY','K80','SYM','GTR','TrN','TrNef','TVM','TIM','K81uf','K81'] #suported for phyml, weighbor, raxml and mrbayes 
  if (esta_em_programAllDefault(model, modelAllDefault)):
    return 1
  else:
    print "The model is unrecognizable"
    sys.exit(2)
    
def modelgenerator_aa(model):
  modelAllDefault = ['BLOSUM62','CPREV','Dayhoff','JTT','MTREV24','VT','WAG','DCMut','RtREV','MtMam','MtArt','MtREV','poisson','jones','BLOSUM','equalin','GTR'] #suported for phyml, weighbor, raxml and mrbayes 
  if (esta_em_modelAllDefault(model, modelAllDefault)):
    return 1
  else:
    print "The model is unrecognizable"
    sys.exit(2)

def esta_em_modelAllDefault(model, modelAllDefault):
  for m in modelAllDefault:
    if model.lower() == m.lower():
      print m
      return 1
  return 0    
  
def make_dir(dirout, filename): 
#  sh.rmtree(dirout,ignore_errors=True)
  if not (os.path.isdir(dirout)):
    os.mkdir(dirin)
  if not (os.path.isfile(filename)):
    sh.copy(filename, dirout)

def lset_rates_mrbayes(rates_mrbayes):
  ratesAllDefault = ['Equal','Gamma','Propinv','Invgamma','Adgamma'] #suported for mrbayes
  if (esta_em_modelAllDefault(rates_mrbayes, ratesAllDefault)):
    return 1
  else:
    print "The rates for mrbayes is unrecognizable"
    sys.exit(2)

def rrates_raxml_aa(rates_raxml_aa):
  ratesAllDefault = ['PROTCAT','PROTCATI','PROTGAMMA','PROTGAMMAI'] #suported for raxml
  if (esta_em_modelAllDefault(rates_raxml_aa, ratesAllDefault)):
    return 1
  else:
    print "The rates for raxml is unrecognizable"
    sys.exit(2)
    
def ffreq_raxml_aa(freq_raxml_aa):
  freqAllDefault = ['F'] #suported for raxml
  if (esta_em_modelAllDefault(freq_raxml_aa, freqAllDefault)):
    return 1
  else:
    print "The frequency for raxml is unrecognizable"
    sys.exit(2)

def rrates_raxml_nucl(rates_raxml_nucl):
  ratesAllDefault = ['CAT','CATI','GAMMA','GAMMAI'] #suported for raxml
  if (esta_em_modelAllDefault(rates_raxml_nucl, ratesAllDefault)):
    return 1
  else:
    print "The rates for raxml is unrecognizable"
    sys.exit(2)

def rrates_paup_ml_nucl(rates_paup_ml_nucl):
  ratesAllDefault = ['Equal','Gamma','SiteSpec'] #suported for paup ML nucl
  if (esta_em_modelAllDefault(rates_paup_ml_nucl, ratesAllDefault)):
    return 1
  else:
    print "The rates for raxml is unrecognizable"
    sys.exit(2)

def main():

  #usage = "python %prog [-h] [-t] data_type [-i] file [-o] dirout [-p] phyml [--mg] model [--bp] bootstrap [--nb] nb_categ [--a] alpha [--in] invar"
  #usage = "%prog [-t] data_type [-o] dirout [-p] program [options] <multifasta.fasta>"
  usage = "%prog [-t] data_type [-o] dirout [-a] alignment [-p] program [-c] trimmer [options] <multifasta.fasta>"
  #python arpa.py -t aa -o output_dir -a mafft -p raxml -t total <rh.fasta>
  parser = OptionParser(usage)
  parser.add_option("-t", dest="data_type", help="amino acid or nucluotide: aa/nucl")
  #parser.add_option("-i", dest="filename", help="a fasta file to process", metavar="FILE")
  parser.add_option("-o", dest="directory", help="directory for store the results", )
  parser.add_option("-a", dest="alignment", help="alignment program: alignm/clustalw/lobster/mafft/muscle/probcons/tcoffee")
  parser.add_option("-c", dest="trimmer", help="trimming and curate program /total/gblock/trimai. total is for the complete sequence")
  parser.add_option("-p", dest="program", help="phylogenetic program: garli/mrbayes/paup_nj/paup_mp/paup_ml/phylip_nj/phylip_mp/phylip_ml/phyml/raxml/weighbor/algorithms_(aa/nucl)_1(phyml,paup_nj,paup_mp)/algorithms_(aa/nucl)_2(paup_nj,weighbor,raxMl)/algorithms_(aa/nucl)_3(all)")
  parser.add_option("--mg", dest="model", help="evolutionary model name")
  parser.add_option("--bp", dest="bootstrap", type="int", help="bootstrap values")
  parser.add_option("--ngen", dest="ngeneration", type="int", help="generation number (mrbayes)")
  parser.add_option("--printfreq", dest="printfreq", type="int", help="how often information about the chain is printed to the screen (mrbayes)")
  parser.add_option("--samplefreq", dest="samplefreq", type="int", help="how often the Markov chain is sampled (mrbayes)")
  parser.add_option("--nchains", dest="nchains", type="int", help="how many chains are run for each analysis for the MCMCMC variant (mrbayes)")                                        
  parser.add_option("--burnin", dest="burnin", type="int", help="the number of samples that will be discarded when convergence diagnostics are calculated (mrbayes)")                                         
  parser.add_option("--nruns", dest="nruns", type="int", help="how many independent analyses are started simultaneously (mrbayes)")                                         
  parser.add_option("--rates_mrbayes", dest="rates_mrbayes", help="sets the model for among-site rate variation: Equal,Gamma,Propinv,Invgamma,Adgamma (mrbayes)")
  parser.add_option("--nb", dest="nb_categ", type="int", help="number of substitution rate categories (phyml, raxml)")
  parser.add_option("--a", dest="alpha", type="float", help="gamma distribution values (phyml, paup_ml)")
  parser.add_option("--in", dest="invar", type="float", help="proportion of invariable sites (phyml)")
  parser.add_option("--rates_raxml_aa", dest="rates_raxml_aa", help="substitution rates: PROTCAT,PROTCATI,PROTGAMMA,PROTGAMMAI (raxml)")
  parser.add_option("--rates_raxml_nucl", dest="rates_raxml_nucl", help="substitution rates: CAT,CATI,GAMMA,GAMMAI (raxml)")
  parser.add_option("--freq_raxml_aa", dest="freq_raxml_aa", help="use empirical base frequencies: F (raxml)")
  parser.add_option("--kappa", dest="kappa", type="int", help="transition/transversion ratio, only for DNA sequences (phyml)")
  parser.add_option("--rates_paup_ml_nucl", dest="rates_paup_ml_nucl", help="sets the model for among-site rate variation: Equal,Gamma,SiteSpec (paup_ml)")
  parser.add_option("-v", action="store_true", dest="verbose")
  parser.add_option("-q", action="store_false", dest="verbose")
  (options, args) = parser.parse_args()
  if len(args) != 1: 
      parser.error("Incorrect number of arguments")
      sys.exit(2)

  #4 parametros obrigatorios
  data_type = options.data_type
  dirout = options.directory
  filename = sys.argv[len(sys.argv)-1] #options.filename
  alignment = options.alignment
  program = options.program
  trimmer = options.trimmer
  model = options.model
  bootstrap = options.bootstrap
  ngeneration = options.ngeneration
  printfreq = options.printfreq
  samplefreq = options.samplefreq
  nchains = options.nchains
  burnin = options.burnin
  nruns = options.nruns
  rates_mrbayes = options.rates_mrbayes
  nb_categ = options.nb_categ
  alpha = options.alpha
  invar = options.invar
  rates_raxml_aa = options.rates_raxml_aa
  freq_raxml_aa = options.freq_raxml_aa
  kappa = options.kappa
  rates_raxml_nucl = options.rates_raxml_nucl
  rates_paup_ml_nucl = options.rates_paup_ml_nucl


  global df
  global dataflow_tag 
  
#******************************* DATAFLOW *******************************
  def randomString(stringLength=10):
    """Generate a random string of fixed length """
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(stringLength))

  dataflow_tag = "rxml"#randomString(10)
  df = Dataflow(dataflow_tag)


# # #Validando alinhamento (filogenetico)
# #************************BEGIN TRANSFORMATION 1*********************************
# #tambem pode ser NUMERIC/TEXT o attributetype
  tf1 = Transformation("ValidationModule_"+dataflow_tag)
  tf1_input = Set("iValidationModule_"+dataflow_tag, SetType.INPUT,
     [ Attribute("Alignmt", AttributeType.TEXT),
       Attribute("Trimmer", AttributeType.TEXT),
       Attribute("Program", AttributeType.TEXT)])
  tf1_output = Set("oValidationModule_"+dataflow_tag, SetType.OUTPUT,
     [ Attribute("Alignmt", AttributeType.TEXT),
       Attribute("Trimmer", AttributeType.TEXT),
       Attribute("Program", AttributeType.TEXT)])
  tf1.set_sets([tf1_input, tf1_output])
  df.add_transformation(tf1)
# #************************END TRANSFORMATION 1***********************************

# #************************BEGIN TRANSFORMATION 2*********************************
# #tambem pode ser NUMERIC/TEXT o attributetype
  tf2 = Transformation("RemovePipeModule_"+dataflow_tag)
  tf2_input = Set("iRemovePipeModule_"+dataflow_tag, SetType.INPUT,
     [ Attribute("dirin", AttributeType.TEXT)])
  tf2_output = Set("oRemovePipeModule_"+dataflow_tag, SetType.OUTPUT,
      [ Attribute("outtext", AttributeType.TEXT)])
  tf2.set_sets([tf2_input, tf2_output])
   #tf2.set_dependency(tf1_output)
  df.add_transformation(tf2)

# #************************END TRANSFORMATION 2***********************************

# # #************************BEGIN TRANSFORMATION 3*********************************
# # #tambem pode ser NUMERIC/TEXT o attributetype
# # mafft*



  tf3 = Transformation("AlignmentModule_"+dataflow_tag)
  tf3_input = Set("iAlignmentModule_"+dataflow_tag, SetType.INPUT,
      [Attribute("dirin", AttributeType.TEXT),
      Attribute("alignment", AttributeType.TEXT),
      Attribute("code", AttributeType.TEXT)])
  tf3_output = Set("oAlignmentModule_"+dataflow_tag, SetType.OUTPUT,
      [Attribute("Alignment", AttributeType.TEXT), 
      Attribute("Dir", AttributeType.TEXT),
      Attribute("code", AttributeType.TEXT)])
  tf3.set_sets([tf3_input, tf3_output])
  # tf2_output.set_type(SetType.INPUT)
  # tf2_output.dependency=tf2._tag
  # tf2.set_sets([tf2_output, tf3_input, tf3_output])
  df.add_transformation(tf3)


# # #************************END TRANSFORMATION 3***********************************

# # #************************BEGIN TRANSFORMATION 4*********************************
# # #tambem pode ser NUMERIC/TEXT o attributetype
# # readseq*
  tf4 = Transformation("ConverterModule_"+dataflow_tag)
  tf4_input = Set("iConverterModule_"+dataflow_tag, SetType.INPUT,
    [ Attribute("Dirin", AttributeType.TEXT),
     Attribute("Path_alignment", AttributeType.TEXT),
     Attribute("trimmer", AttributeType.TEXT)])
  tf4_output = Set("oConverterModule_"+dataflow_tag, SetType.OUTPUT,
   [ Attribute("Sequences_Names", AttributeType.TEXT),
     Attribute("NXS_file", AttributeType.TEXT),
     Attribute("Phy_file", AttributeType.TEXT)])
  tf4.set_sets([tf4_input, tf4_output])
   #tf4.set_dependency(tf3_output)
  df.add_transformation(tf4)
# # #************************END TRANSFORMATION 4***********************************

# # # #************************BEGIN TRANSFORMATION 5*********************************
# # # #tambem pode ser NUMERIC/TEXT o attributetype
  tf5 = Transformation("ModelGeneratorModule_"+dataflow_tag)
  tf5_input = Set("iModelGeneratorModule_"+dataflow_tag, SetType.INPUT,
    [ Attribute("Dirin", AttributeType.TEXT)])
  tf5_output = Set("oModelGeneratorModule_"+dataflow_tag, SetType.OUTPUT,
    [ Attribute("Model", AttributeType.TEXT)])
  tf5.set_sets([tf5_input, tf5_output])
   #tf3.set_dependency(tf4_output)
  df.add_transformation(tf5)
# # #************************END TRANSFORMATION 5***********************************

# # # #************************BEGIN TRANSFORMATION 6*********************************
# # # #tambem pode ser NUMERIC/TEXT o attributetype
  tf6 = Transformation("ProgramExecuteModule_"+dataflow_tag)
  tf6_input = Set("iProgramExecuteModule_"+dataflow_tag, SetType.INPUT,
    [ Attribute("Program", AttributeType.TEXT)])
  tf6_output = Set("oProgramExecuteModule_"+dataflow_tag, SetType.OUTPUT,
    [ Attribute("Program", AttributeType.TEXT),
      Attribute("Tree", AttributeType.TEXT)])
  tf6.set_sets([tf6_input, tf6_output])
   #tf3.set_dependency(tf4_output)
  df.add_transformation(tf6)
# # #************************END TRANSFORMATION 5***********************************

# # # #************************BEGIN TRANSFORMATION 7*********************************
  tf7 = Transformation("TelemetryModule_"+dataflow_tag)
  tf7_input = Set("iTelemetry_"+dataflow_tag, SetType.INPUT,
      [Attribute("Test", AttributeType.NUMERIC)])
  tf7_output = Set("oTelemetry_"+dataflow_tag, SetType.OUTPUT,
      [Attribute("Timestamp", AttributeType.TEXT),
      Attribute("scputimes_nice", AttributeType.TEXT),
      Attribute("svmem_percent", AttributeType.TEXT),
      Attribute("sdiskio_read_time", AttributeType.TEXT),
      Attribute("sdiskio_write_time", AttributeType.TEXT)])
  tf7.set_sets([tf7_input, tf7_output])
  df.add_transformation(tf7)
# # #************************END TRANSFORMATION 7***********************************

  df.save()

###############################################################
# Data Transformation 1 - Task 1 - Validando alignment
##############################################################
  

  t1 = Task(1, dataflow_tag, "ValidationModule_"+dataflow_tag, "t1")
  t1_input = DataSet("iValidationModule_"+dataflow_tag, [Element([alignment, trimmer, program])])
  t1.add_dataset(t1_input)
  t1.begin()
  print "alinhamento: "+alignment
  tipo_alinhamento = validate_parametersA(alignment) #atividade sciphy
  tipo_trimmer = validate_parametersT(trimmer)
  tipo_programa = validate_parameters(program)
  make_dir(dirout, filename)

  t1_output = DataSet("oValidationModule_"+dataflow_tag, [Element([tipo_alinhamento, tipo_trimmer, tipo_programa])])
  t1.add_dataset(t1_output)
  t1.end()

  if data_type == 'nucl':
    if alphabet_nucl(filename) == True:
      if model is not None:
        result = modelgenerator_nucl(model)
        
        #--if rates_raxml_aa is not None:
        #  print "Pass rates_raxml_nucl"
        #  sys.exit(2)
        #if rates_raxml_nucl is not None:
        #  rrates_raxml_nucl(rates_raxml_nucl)
        #if rates_mrbayes is not None:    
        #  lset_rates_mrbayes(rates_mrbayes)
        #if rates_paup_ml_nucl is not None:    
        #--  rrates_paup_ml_nucl(rates_paup_ml_nucl)
        #make_dir(dirin, filename)
        #mafft_clean_readseq(dirout)
        remove_pipe(dirout, filename, alignment, trimmer)
        program_execute_nucl(dirout, model, program, bootstrap, ngeneration, printfreq, samplefreq, nchains, burnin, nruns, rates_mrbayes, nb_categ, alpha, invar, kappa, rates_raxml_nucl, rates_paup_ml_nucl)
      if model is None:
        #--if rates_raxml_nucl is not None:
        #  rrates_raxml_nucl(rates_raxml_nucl)
        #if rates_mrbayes is not None: 
        #  lset_rates_mrbayes(rates_mrbayes)
        #if rates_paup_ml_nucl is not None:    
        #--  rrates_paup_ml_nucl(rates_paup_ml_nucl)  
        #make_dir(dirin, filename)
        #mafft_clean_readseq(dirout)
        remove_pipe(dirout, filename, alignment, trimmer)    
        modelmg = modelgenerator_execute(dirout)
        program_execute_nucl(dirout, modelmg, program, bootstrap, ngeneration, printfreq, samplefreq, nchains, burnin, nruns, rates_mrbayes, nb_categ, alpha, invar, kappa, rates_raxml_nucl, rates_paup_ml_nucl)
  elif data_type == 'aa':
    if alphabet_aa(filename) == True:
      if model is not None:

        result = modelgenerator_aa(model)

        print "MODELO: "+ model
        print "fim da task modelgenerator"

        #modelgenerator_aa(model)
        #--if rates_raxml_nucl is not None:
        #  print "Pass rates_raxml_aa"
        #  sys.exit(2)
        #if freq_raxml_aa is not None:
        #  ffreq_raxml_aa(freq_raxml_aa)
        #if rates_raxml_aa is not None:
        #  rrates_raxml_aa(rates_raxml_aa)
        #if rates_mrbayes is not None:
        #--  lset_rates_mrbayes(rates_mrbayes)
        #make_dir(dirin, filename)
        #mafft_clean_readseq(dirout)

        remove_pipe(dirout, filename, alignment, trimmer)    
        program_execute_aa(dirout, model, program, bootstrap, ngeneration, printfreq, samplefreq, nchains, burnin, nruns, rates_mrbayes, nb_categ, alpha, invar, rates_raxml_aa, freq_raxml_aa)
      
      if model is None:

        remove_pipe(dirout, filename, alignment, trimmer)

        # t6 = Task(6, dataflow_tag, "AlignmentModule_"+dataflow_tag)
        # t6_input = DataSet("iAlignmentModule_"+dataflow_tag, [Element([dirout, alignment, trimmer])])
        # t6.add_dataset(t6_input)
        # t6.begin()
        modelmg = modelgenerator_execute(dirout)
        # t6_output = DataSet("oAlignmentModule_"+dataflow_tag, [Element([modelmg])])
        # t6.add_dataset(t6_output)
        # t6.end()
        
        
        #--if freq_raxml_aa is not None:
        #  ffreq_raxml_aa(freq_raxml_aa)
        #if rates_raxml_aa is not None:
        #  rrates_raxml_aa(rates_raxml_aa)
        #if rates_mrbayes is not None:
        #--  lset_rates_mrbayes(rates_mrbayes)
        #make_dir(dirin, filename)
        #mafft_clean_readseq(dirout)

        program_execute_aa(dirout, modelmg, program, bootstrap, ngeneration, printfreq, samplefreq, nchains, burnin, nruns, rates_mrbayes, nb_categ, alpha, invar, rates_raxml_aa,freq_raxml_aa)

        # t6 = Task(6, dataflow_tag, "ProgramExecute")
        # t6_input = DataSet("iProgramExecute", [Element(["hello"])])
        # t6.add_dataset(t6_input)
        # t6.begin()
        
        # t6_output = DataSet("oProgramExecute", [Element(["hi"])])
        # t6.add_dataset(t6_output)
        # t6.end()

  else:
    print "Pass 'aa' or 'nucl' as data_type"
    sys.exit(2)
  #-------------------------------------------------------------------------------
  # Executando Programas de Alinhamentos
#************************END TRANSFORMATION 1********************************************

  #-------------------------------------------------------------------------------
  #PARTE I: OBRIGATORIO
  #-------------------------------------------------------------------------------
  # Removendo pipes e limpamdo fasta
  #-------------------------------------------------------------------------------
def remove_pipe(dirin, filename, alignment, trimmer):
  import makeRemovePipe_aa
  print "DIRIN-----------------------:> "+dirin
  print "FILENAME "+ filename
  sequencia_entrada = open(filename, "r")
  sequencia_lida = sequencia_entrada.readlines()
  sequencia_lida = ' '.join(map(str, sequencia_lida))
  sequencia_lida = sequencia_lida.rstrip('\n')
  sequencia_lida = sequencia_lida.rstrip(',')
  print sequencia_lida
  ###############################################################
  # Data Transformation 2 - Task 5 - Limpeza
  ##############################################################

  t2 = Task(2, dataflow_tag, "RemovePipeModule_"+dataflow_tag, "t2")
  t2_input = DataSet("iRemovePipeModule_"+dataflow_tag, [Element([filename])])
  t2.add_dataset(t2_input)
  t2.begin()
  corrected_file = makeRemovePipe_aa.paramModule(dirin)
  t2_output = DataSet("oRemovePipeModule_"+dataflow_tag, [Element([dirin])])
  t2.add_dataset(t2_output)
  t2.end()

  # 1 = Task(1, dataflow_tag, "ValidationModule_"+dataflow_tag, "t1")
  # t1_input = DataSet("iValidationModule_"+dataflow_tag, [Element([alignment, trimmer, program])])
  # t1.add_dataset(t1_input)
  # t1.begin()
  # print "alinhamento: "+alignment
  # tipo_alinhamento = validate_parametersA(alignment) #atividade sciphy
  # tipo_trimmer = validate_parametersT(trimmer)
  # tipo_programa = validate_parameters(program)


  t3 = Task(3, dataflow_tag, "AlignmentModule_"+dataflow_tag, "t3")
  t3_input = DataSet("iAlignmentModule_"+dataflow_tag, [Element([dirin, alignment, sequencia_lida])])
  t3.add_dataset(t3_input)
  t3.begin()
  
  test = execute_alignment(dirin, corrected_file, alignment, trimmer)

  # equencia_entrada = open(filename, "r")
  # sequencia_lida = sequencia_entrada.readlines()
  # x = ' '.join(map(str, sequencia_lida))
  # x = x.rstrip('\n')
  # x = x.rstrip(',')
  saidaAlinhamento = open("out/file.aln", "r")
  oalignment   = saidaAlinhamento.readlines()
  oalignment = ' '.join(map(str, oalignment))
  oalignment = oalignment.rstrip('\n')
  oalignment = oalignment.rstrip(',')
  print oalignment

  t3_output = DataSet("oAlignmentModule_"+dataflow_tag, [Element([alignment, dirin, oalignment])])
  t3.add_dataset(t3_output)
  t3.end()
  #-------------------------------------------------------------------------------
  # Executando Programas de Alinhamentos
  #-------------------------------------------------------------------------------
def execute_alignment(dirin, corrected_file, alignment, trimmer):
  print "EXECUTANDO ALINHAMENTO"
  if alignment == 'alignm':
    import makeAlignm
    makeAlignm.paramModuleExecution(dirin)    
    for m in os.listdir(dirin):
#      if m.endswith('.alignm'):
      if m.endswith('.aln'):                                                    
        path_alignment = os.path.join(dirin, m)
        os.chmod(path_alignment, 0755)   
        execute_trimming(dirin, corrected_file, path_alignment, trimmer)

  if alignment == 'clustalw':
    import makeClustalw
    makeClustalw.paramModuleExecution(dirin)
    for m in os.listdir(dirin):
      if m.endswith('.aln'):
        path_alignment = os.path.join(dirin, m)
        os.chmod(path_alignment, 0755)  
        execute_trimming(dirin, corrected_file, path_alignment, trimmer)

  if alignment == 'mafft':
    import makeMafft_aa
    print "Executando mafft em " +dirin
    alinhamento = makeMafft_aa.paramModuleExecution(dirin)
    print "ALINHAMENTO:****** "+str(alinhamento)
    for m in os.listdir(dirin):
      #original if m.endswith('.mafft'):
      if m.endswith('.aln'):
        print1 = path_alignment = os.path.join(dirin, m)
        print2 = os.chmod(path_alignment, 0755)  
        print "corrected file " +str(corrected_file)
        print "print1: "+print1
        print "print2: "+str(print2)
#        readseq(dirin, path_alignment)
      #*****************************************************************READ SEQ
        execute_trimming(dirin, corrected_file, path_alignment, trimmer)
      #*************************************************************************
  if alignment == 'muscle':
    import makeMuscle
    makeMuscle.paramModuleExecution(dirin)
    for m in os.listdir(dirin):
#      if m.endswith('.muscle'):
      if m.endswith('.aln'):
        path_alignment = os.path.join(dirin, m)
        os.chmod(path_alignment, 0755)  
        execute_trimming(dirin, corrected_file, path_alignment, trimmer)

  if alignment == 'probcons':
    import makeProbcons_aa
    makeProbcons_aa.paramModuleExecution(dirin)
    for m in os.listdir(dirin):
#original      if m.endswith('.probcons'):
      if m.endswith('.aln'):
        path_alignment = os.path.join(dirin, m)
        os.chmod(path_alignment, 0755)  
        execute_trimming(dirin, corrected_file, path_alignment, trimmer)

  if alignment == 'tcoffee':
    import makeTcoffee
    print 'Execuntando T-Coffee em '+dirin
    makeTcoffee.paramModuleExecution(dirin)
    print 'Gerado'
    for m in os.listdir(dirin):
#original      if m.endswith('.tcoffee'):
      if m.endswith('.aln'):                 
        path_alignment = os.path.join(dirin, m)
        os.chmod(path_alignment, 0755)  
        execute_trimming(dirin, corrected_file, path_alignment, trimmer)

  #-------------------------------------------------------------------------------
  # Executando Trimming
  #-------------------------------------------------------------------------------
  #task transformation readseq
def execute_trimming(dirin, corrected_file, path_alignment, trimmer):
  t4 = Task(4, dataflow_tag, "ConverterModule_"+dataflow_tag)
  t4_input = DataSet("iConverterModule_"+dataflow_tag, [Element([dirin, path_alignment, trimmer])])
  t4.add_dataset(t4_input)
  t4.begin()

  # t8 = Task(8, dataflow_tag, "ConverterModule_"+dataflow_tag)
  # t8_input = DataSet("iConverterModule_"+dataflow_tag, [Element([dirin, path_alignment])])
  # t8.add_dataset(t8_input)
  # t8.begin()


  if trimmer == 'trimal':      
    import makeTrimal
    makeTrimal.paramModuleExecution(path_alignment)
    for m in os.listdir(dirin):
#      if m.endswith('.trimal'):
      if m.endswith('.aln'):
        path_trimmer = os.path.join(dirin, m)
        os.chmod(path_trimmer, 0755)  
        result = readseq(dirin, path_trimmer)

  if trimmer == 'gblocks':
    import makeGblocks
    makeGblocks.paramModuleExecution(path_alignment)
    for m in os.listdir(dirin):
#      if m.endswith('-gb1'):
      if m.endswith('.aln'):
        path_trimmer = os.path.join(dirin, m)  
        os.chmod(path_trimmer, 0755)  
        readseq(dirin, path_trimmer)  

  if trimmer == 'total':
    read = readseq(dirin, path_alignment)  
  
  # t8_output = DataSet("oConverterModule_"+dataflow_tag, [Element([0, "file"])])
  # t8.add_dataset(t8_output)
  # t8.end()
#####################################################################################
# Pegando dados dos arquivos que o sciphy cria (extensão .phy e .nxs)
# codigo adicionado para inserir no banco da dfanalyzer
  sequencias = ""
  nxs_file = ""
  phy_file = ""

  nome_nxs = open("out/file.aln_nxs", "r")
  for line in nome_nxs:
    #print(line)
    if "Name:" in line:
      sequencias = sequencias+line[line.find("[out/file.aln -- data title]\n:")+1:line.find("\nbegin data;")]
  nome_nxs.close()

  nxs = open("out/file.aln_nxs", "r")
  for line in nxs:
    nxs_file = nxs_file+line
  nxs.close()

  phy = open("out/file.aln_phy", "r")
  for line in phy:
    phy_file = phy_file+line
  phy.close()
#####################################################################################

  t4_output = DataSet("oConverterModule_"+dataflow_tag, [Element([sequencias, nxs_file, phy_file])])
  t4.add_dataset(t4_output)
  t4.end()
  #if trimmer is None:
  #  readseq(dirin, path_alignment)    
  #-------------------------------------------------------------------------------
  # Executando Readseq
  #-------------------------------------------------------------------------------
def readseq(dirin, path_trimmer):
  import makeReadseq_aa
  print "DIRIN READSEQ: "+ dirin
  print "PATH_TRIMMER: "+ path_trimmer
  makeReadseq_aa.paramModuleReadseq(path_trimmer)

  

  #-------------------------------------------------------------------------------
  # Executando Modelgenerator
  #-------------------------------------------------------------------------------
def modelgenerator_execute(dirin):
  t5 = Task(5, dataflow_tag, "ModelGeneratorModule_"+dataflow_tag)
  t5_input = DataSet("iModelGeneratorModule_"+dataflow_tag, [Element([dirin])])
  t5.add_dataset(t5_input)
  t5.begin()

  import makeModelgenerator_aa
  model_found = makeModelgenerator_aa.paramModuleModelgenerator(dirin)
  print "1-> "+ model_found

  t5_output = DataSet("oModelGeneratorModule_"+dataflow_tag, [Element([model_found])])
  t5.add_dataset(t5_output)
  t5.end()

  return model_found
  
#-------------------------------------------------------------------------------
#PARTE II: PARTE ELETIVA: POR ALGORITMO
#-------------------------------------------------------------------------------
  #   4.- Executando Phyml
  #-------------------------------------------------------------------------------
def program_execute_aa(dirin, model, program, bootstrap, ngeneration, printfreq, samplefreq, nchains, burnin, nruns, rates_mrbayes, nb_categ, alpha, invar, rates_raxml_aa, freq_raxml_aa):
  t6 = Task(6, dataflow_tag, "ProgramExecuteModule_"+dataflow_tag)
  t6_input = DataSet("iProgramExecuteModule_"+dataflow_tag, [Element([program])])
  t6.add_dataset(t6_input)
  t6.begin()
  
  if program == 'phyml':
    if bootstrap is None:
      bootstrap = '100'
    if nb_categ is None:
      nb_categ = '4'
    if alpha is None:
      alpha = '1.0'
    if invar is None:
      invar = '0.0'
    import makePhyml_aa_last 
    makePhyml_aa_last.ModulePhyml(dirin, model, bootstrap, nb_categ, alpha, invar)
  
  if program == 'phylip_nj':
    if bootstrap is None:
      bootstrap = '10000'
    import makePhylipNJParamModule_aa
    makePhylipNJParamModule_aa.ModulePhylipNJ(dirin, bootstrap)

  if program == 'phylip_mp':
    if bootstrap is None:
      bootstrap = '500'
    import makePhylipMPParamModule_aa
    makePhylipMPParamModule_aa.ModulePhylipMP(dirin, bootstrap)

  if program == 'phylip_ml':
    if bootstrap is None:
      bootstrap = '100'
    import makePhylipMLParamModule_aa
    makePhylipMLParamModule_aa.ModulePhylipML(dirin, bootstrap)
#por enquanto falta incrementar os modelos

  if program == 'paup_nj':
    if bootstrap is None:
      bootstrap = '10000'
    import makePaupNJParamModule_aa
    makePaupNJParamModule_aa.ModulePaupNJ(dirin, bootstrap)

  if program == 'paup_mp':
    if bootstrap is None:
      bootstrap = '500'
    import makePaupMPParamModule_aa
    makePaupMPParamModule_aa.ModulePaupMP(dirin, bootstrap)

  if program == 'weighbor':
    if bootstrap is None:
      bootstrap = '100'
    if nb_categ is None:
      nb_categ = '6'
    import makeWeighbor_aa
    makeWeighbor_aa.ModuleWeighbor(dirin, model, bootstrap, nb_categ)

  if program == 'raxml':
    if bootstrap is None:
      bootstrap = '100'
    if rates_raxml_aa is None:
      rates_raxml_aa = 'PROTGAMMA'
      nb_categ = '4'
    if rates_raxml_aa is 'PROTGAMMA' or 'PROTGAMMAI':
      nb_categ = '4'
    if freq_raxml_aa is None or 'f':
      freq_raxml_aa = 'F'
    if nb_categ is None:
      nb_categ = '4'
    import makeRaxml_aa
    makeRaxml_aa.ModuleRaxml(dirin, model, bootstrap, nb_categ, rates_raxml_aa, freq_raxml_aa)
    raxmltree = open("RAxML_bestTree.file.aln_phy_raxml_tree1.singleTree", "r")
    for line in raxmltree:
      t6_output = DataSet("oProgramExecuteModule_"+dataflow_tag, [Element([program, line])])
      t6.add_dataset(t6_output)
      t6.end()
    
  if program == 'garli':
    if bootstrap is None:
      bootstrap = '100'
    if nb_categ is None:
      nb_categ = '4'
    import makeGarli_aa
    makeGarli_aa.ModuleGarli(dirin, model, bootstrap, nb_categ)
    
  if program == 'mrbayes':
    if ngeneration is None:
      ngeneration = '10000'
    if nb_categ is None:
      nb_categ = '4'
    if printfreq is None:
      printfreq = '100'
    if samplefreq is None:
      samplefreq = '100'
    if nchains is None:
      nchains = '4'
    if burnin is None:
      burnin = '10'
    if nruns is None:
      nruns = '2'
    if rates_mrbayes is None:
      rates_mrbayes = 'Equal'
    import makeMrBayes_aa
    makeMrBayes_aa.ModuleMrBayes(dirin, model, ngeneration, nb_categ, printfreq, samplefreq, nchains, burnin, nruns, rates_mrbayes)
    
  if program == 'algorithms_aa_1':
    bootstrap = '100'
    nb_categ = '4'
    alpha = '1.0'
    invar = '0.0'
    import makePhyml_aa_last 
    makePhyml_aa_last.ModulePhyml(dirin, model, bootstrap, nb_categ, alpha, invar)
    bootstrap = '10000'
    import makePaupNJParamModule_aa
    makePaupNJParamModule_aa.ModulePaupNJ(dirin, bootstrap)
    bootstrap = '500'
    import makePaupMPParamModule_aa
    makePaupMPParamModule_aa.ModulePaupMP(dirin, bootstrap)

  if program == 'algorithms_aa_2':
    bootstrap = '100'
    nb_categ = '6'
    import makeWeighbor_aa
    bootstrap = '10000'
    import makePaupNJParamModule_aa
    makePaupNJParamModule_aa.ModulePaupNJ(dirin, bootstrap)
    makeWeighbor_aa.ModuleWeighbor(dirin, model, bootstrap, nb_categ)
    bootstrap = '100'
    rates_raxml_aa = 'PROTGAMMA'
    freq_raxml_aa = 'F'
    nb_categ = '4'
    import makeRaxml_aa
    makeRaxml_aa.ModuleRaxml(dirin, model, bootstrap, nb_categ, rates_raxml_aa, freq_raxml_aa)

  if program == 'algorithms_aa_3':
    bootstrap = '100'
    nb_categ = '4'
    alpha = '1.0'
    invar = '0.0'
    import makePhyml_aa_last 
    makePhyml_aa_last.ModulePhyml(dirin, model, bootstrap, nb_categ, alpha, invar)
    bootstrap = '10000'
    import makePaupNJParamModule_aa
    makePaupNJParamModule_aa.ModulePaupNJ(dirin, bootstrap)
    bootstrap = '500'
    import makePaupMPParamModule_aa
    makePaupMPParamModule_aa.ModulePaupMP(dirin, bootstrap)
    bootstrap = '100'
    nb_categ = '6'
    import makeWeighbor_aa
    makeWeighbor_aa.ModuleWeighbor(dirin, model, bootstrap, nb_categ)
    bootstrap = '100'
    rates_raxml_aa = 'PROTGAMMA'
    freq_raxml_aa = 'F'
    nb_categ = '4'
    import makeRaxml_aa
    makeRaxml_aa.ModuleRaxml(dirin, model, bootstrap, nb_categ, rates_raxml_aa, freq_raxml_aa)
    ngeneration = '10000'
    nb_categ = '4'
    printfreq = '100'
    samplefreq = '100'
    nchains = '4'
    burnin = '10'
    nruns = '2'
    rates_mrbayes = 'Equal'
    import makeMrBayes_aa
    makeMrBayes_aa.ModuleMrBayes(dirin, model, ngeneration, nb_categ, printfreq, samplefreq, nchains, burnin, nruns, rates_mrbayes)



def program_execute_nucl(dirin, model, program, bootstrap, ngeneration, printfreq, samplefreq, nchains, burnin, nruns, rates_mrbayes, nb_categ, alpha, invar, kappa, rates_raxml_nucl, rates_paup_ml_nucl):
  if program == 'phyml':
    if bootstrap is None:
      bootstrap = '100'
    if nb_categ is None:
      nb_categ = '1'
    if alpha is None:
      alpha = '1.0'
    if kappa is None:
      kappa = '4.0'
    import makePhyml_nucl 
    makePhyml_nucl.ModulePhyml(dirin, model, bootstrap, nb_categ, alpha, kappa)
  
  if program == 'phylip_nj':
    if bootstrap is None:
      bootstrap = '10000'
    import makePhylipNJParamModule_nucl
    makePhylipNJParamModule_nucl.ModulePhylipNJ(dirin, bootstrap)

  if program == 'phylip_mp':
    if bootstrap is None:
      bootstrap = '500'
    import makePhylipMPParamModule_nucl
    makePhylipMPParamModule_nucl.ModulePhylipMP(dirin, bootstrap)

  if program == 'phylip_ml':
    if bootstrap is None:
      bootstrap = '100'
    import makePhylipMLParamModule_nucl
    makePhylipMLParamModule_nucl.ModulePhylipML(dirin, bootstrap)
#por enquanto falta incrementar os modelos

  if program == 'paup_nj':
    if bootstrap is None:
      bootstrap = '10000'
    import makePaupNJParamModule_nucl
    makePaupNJParamModule_nucl.ModulePaupNJ(dirin, bootstrap)

  if program == 'paup_mp':
    if bootstrap is None:
      bootstrap = '500'
    import makePaupMPParamModule_nucl
    makePaupMPParamModule_nucl.ModulePaupMP(dirin, bootstrap)

  if program == 'paup_ml':
    if bootstrap is None:
      bootstrap = '100'
    if nb_categ is None:
      nb_categ = '4'
    if alpha is None:
      alpha = '0.5'
    if invar is None:
      invar = '0'
    if rates_paup_ml_nucl is None:
      rates_paup_ml_nucl = 'Equal'
    import makePaupML_nucl
    makePaupML_nucl.ModulePaupML(dirin, model, bootstrap, nb_categ, rates_paup_ml_nucl, alpha, invar)
    
  if program == 'garli':
    if bootstrap is None:
      bootstrap = '100'
    if nb_categ is None:
      nb_categ = '4'
    import makeGarli_nucl
    makeGarli_nucl.ModuleGarli(dirin, model, bootstrap, nb_categ)
    
  if program == 'weighbor':
    if bootstrap is None:
      bootstrap = '100'
    if nb_categ is None:
      nb_categ = '4'
    import makeWeighbor_nucl
    makeWeighbor_nucl.ModuleWeighbor(dirin, model, bootstrap, nb_categ)

  if program == 'raxml':
    if bootstrap is None:
      bootstrap = '100'
    if model is None or 'GTR':
      model = 'GTR'
    if rates_raxml_nucl is None or 'GAMMA':
      rates_raxml_nucl = 'GAMMA'
#      nb_categ = '4'
#    if rates_raxml_nucl is 'GAMMA' or 'GAMMAI':
#      nb_categ = '4'
    if nb_categ is None:
      nb_categ = '4'
    import makeRaxml_nucl
    makeRaxml_nucl.ModuleRaxml(dirin, model, bootstrap, nb_categ, rates_raxml_nucl)

  if program == 'mrbayes':
    if ngeneration is None:
      ngeneration = '10000'
    if nb_categ is None:
      nb_categ = '4'
    if printfreq is None:
      printfreq = '100'
    if samplefreq is None:
      samplefreq = '100'
    if nchains is None:
      nchains = '4'
    if burnin is None:
      burnin = '10'
    if nruns is None:
      nruns = '2'
    if rates_mrbayes is None:
      rates_mrbayes = 'Equal'
    import makeMrBayes_nucl
    makeMrBayes_nucl.ModuleMrBayes(dirin, model, ngeneration, nb_categ, printfreq, samplefreq, nchains, burnin, nruns, rates_mrbayes)
    
  if program == 'algorithms_nucl_1':
    bootstrap = '100'
    nb_categ = '1'
    alpha = '1.0'
    kappa = '4.0'
    import makePhyml_nucl 
    makePhyml_nucl.ModulePhyml(dirin, model, bootstrap, nb_categ, alpha, kappa)
    bootstrap = '10000'
    import makePaupNJParamModule_nucl
    makePaupNJParamModule_nucl.ModulePaupNJ(dirin, bootstrap)
    bootstrap = '500'
    import makePaupMPParamModule_nucl
    makePaupMPParamModule_nucl.ModulePaupMP(dirin, bootstrap)

  if program == 'algorithms_nucl_2':
    bootstrap = '100'
    nb_categ = '4'
    import makeWeighbor_nucl
    makeWeighbor_nucl.ModuleWeighbor(dirin, model, bootstrap, nb_categ)
    bootstrap = '10000'
    import makePaupNJParamModule_aa
    bootstrap = '100'
    rates_raxml_nucl = 'GAMMA'
    nb_categ = '4'
    import makeRaxml_nucl
    makeRaxml_nucl.ModuleRaxml(dirin, model, bootstrap, nb_categ, rates_raxml_nucl)

  if program == 'algorithms_nucl_3':
    bootstrap = '100'
    nb_categ = '1'
    alpha = '1.0'
    kappa = '4.0'
    import makePhyml_nucl 
    makePhyml_nucl.ModulePhyml(dirin, model, bootstrap, nb_categ, alpha, kappa)
    bootstrap = '10000'
    import makePaupNJParamModule_nucl
    makePaupNJParamModule_nucl.ModulePaupNJ(dirin, bootstrap)
    bootstrap = '500'
    import makePaupMPParamModule_nucl
    makePaupMPParamModule_nucl.ModulePaupMP(dirin, bootstrap)
    bootstrap = '100'
    nb_categ = '4'
    alpha = '0.5'
    invar = '0'
    rates_paup_ml_nucl = 'Equal'
    import makePaupML_nucl
    makePaupML_nucl.ModulePaupML(dirin, model, bootstrap, nb_categ, rates_paup_ml_nucl, alpha, invar)
    bootstrap = '100'
    nb_categ = '4'
    import makeGarli_nucl
    makeGarli_nucl.ModuleGarli(dirin, model, bootstrap, nb_categ)
    bootstrap = '100'
    nb_categ = '4'
    import makeWeighbor_nucl
    makeWeighbor_nucl.ModuleWeighbor(dirin, model, bootstrap, nb_categ)
    bootstrap = '100'
    rates_raxml_nucl = 'GAMMA'
    nb_categ = '4'
    import makeRaxml_nucl
    makeRaxml_nucl.ModuleRaxml(dirin, model, bootstrap, nb_categ, rates_raxml_nucl)
  if program == 'mrbayes':
    ngeneration = '10000'
    nb_categ = '4'
    printfreq = '100'
    samplefreq = '100'
    nchains = '4'
    burnin = '10'
    nruns = '2'
    rates_mrbayes = 'Equal'
    import makeMrBayes_nucl
    makeMrBayes_nucl.ModuleMrBayes(dirin, model, ngeneration, nb_categ, printfreq, samplefreq, nchains, burnin, nruns, rates_mrbayes)

def inicia_sensors(nome_arquivo):
    os.system('python2 sensors_without_kafka.py 20 1')

if __name__ == "__main__":

  arquivos = ['sensors_without_kafka.py']
  processos = []

  for arquivo in arquivos:
    processos.append(threading.Thread(target=inicia_sensors, args=(arquivo,)))

  for processo in processos:
    processo.start()
  
  main()
  os.popen('ps axf | grep sensors_without_kafka.py | grep -v grep | awk \'{print \"kill -9 \" $1}\' | sh')
  
  t7 = Task(7, dataflow_tag, "TelemetryModule_"+dataflow_tag)
  t7.begin()
  with open("/home/luizgustavo/Documents/DfAnalyzer-Bitbucket/SciPhy/sciphy/cgi-bin/telemetria.txt", 'r') as f:
    lista = f.read().splitlines()
    for x in range(len(lista)):
      try:
        if (len(lista[x + 1]) is not None): #se tiver próximo
          lista[x] = lista[x].replace('[', '').replace(']', '')
          info = json.loads(lista[x])
          # t6_output = DataSet("oTelemetry",
         #      [Element([info['timestamp'], info['scputimes_nice'], info['svmem_percent'], info['sdiskio_read_time'], info['sdiskio_write_time']])])
          # t6.add_dataset(t6_output)
          objDate = datetime.datetime.strptime(info['timestamp'], '%Y-%m-%d %H:%M:%S.%f')
          t7.add_telemetry(Telemetry(str(info['timestamp']), "20", "1"))  # date, time, interval and epoch_id
          t7.add_telemetry_cpu(TelemetryCPU(str(info['timestamp']), str(info['scputimes_user']), str(info['scputimes_system']), str(info['scputimes_idle']), str(info['scputimes_steal']))) #date, time, scputimes_user, scputimes_system, scputimes_idle, scputimes_steal
          t7.add_telemetry_memory(TelemetryMemory(str(info['timestamp']), str(info['svmem_total']), str(info['svmem_available']), str(info['svmem_used']))) #date, time, svmem_total , svmem_available, svmem_used
          t7.add_telemetry_disk(TelemetryDisk(str(info['timestamp']), str(info['sdiskio_read_bytes']), str(info['sdiskio_write_bytes']), str(info['sdiskio_busy_time']), str(info['sswap_total']), str(info['sswap_used']))) #date, time, sdiskio_read_bytes, sdiskio_write_bytes, sdiskio_busy_time, sswap_total, sswap_used
          t7.save()

      except IndexError:
        lista[x] = lista[x].replace('[', '').replace(']', '')
        info = json.loads(lista[x])
        # t6_output = DataSet("oTelemetry",
        #         [Element([info['timestamp'], info['scputimes_nice'], info['svmem_percent'], info['sdiskio_read_time'], info['sdiskio_write_time']])])
        # t6.add_dataset(t6_output)
        objDate = datetime.datetime.strptime(info['timestamp'], '%Y-%m-%d %H:%M:%S.%f')
        t7.add_telemetry(Telemetry(str(info['timestamp']), "30", "2"))  # date, time, interval and epoch_id
        # para capturar telemetria da cpu
        t7.add_telemetry_cpu(TelemetryCPU(str(info['timestamp']), str(info['scputimes_user']), str(info['scputimes_system']), str(info['scputimes_idle']), str(info['scputimes_steal']))) #date, time, scputimes_user, scputimes_system, scputimes_idle, scputimes_steal
        t7.add_telemetry_memory(TelemetryMemory(str(info['timestamp']), str(info['svmem_total']), str(info['svmem_available']), str(info['svmem_used']))) #date, time, svmem_total , svmem_available, svmem_used
        t7.add_telemetry_disk(TelemetryDisk(str(info['timestamp']), str(info['sdiskio_read_bytes']), str(info['sdiskio_write_bytes']), str(info['sdiskio_busy_time']), str(info['sswap_total']), str(info['sswap_used']))) #date, time, sdiskio_read_bytes, sdiskio_write_bytes, sdiskio_busy_time, sswap_total, sswap_used
        t7.end()

  os.system('rm file.aln_phy')
  os.system('rm file.aln_nxs')
  os.system('rm file.aln_phyml.sh')
  os.system('rm file.aln_puzzleBoot.sh')
  os.system('rm file.aln_phymlBoot.sh')
  os.system('rm modelgenerator0.out')
  os.system('rm RAxML_bestTree.file.aln_phy_raxml_tree1.singleTree')
  os.system('rm RAxML_bipartitions.file.aln_phy_tree3.BS_TREE')
  os.system('rm RAxML_bipartitionsBranchLabels.file.aln_phy_tree3.BS_TREE')
  os.system('rm RAxML_bootstrap.file.aln_phy_tree2.raxml')
  os.system('rm RAxML_info.file.aln_phy_raxml_tree1.singleTree')
  os.system('rm RAxML_info.file.aln_phy_tree2.raxml')
  os.system('rm RAxML_info.file.aln_phy_tree3.BS_TREE')
  os.system('rm RAxML_log.file.aln_phy_raxml_tree1.singleTree')
  os.system('rm RAxML_parsimonyTree.file.aln_phy_raxml_tree1.singleTree')
  os.system('rm RAxML_result.file.aln_phy_raxml_tree1.singleTree')
  os.system('rm file.aln_treePuzzle.sh')


    