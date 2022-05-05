#!/usr/bin/python

# TITULO            : Geral Pipeline, profile phylogeny
# AUTOR             : Kary Soriano
# DATA              : 07/01/2008
# DIFICULDADE       : 2
# ==============================================================================
# Objetivo do script: Rodado como o programa principal. Executar Mafft, Readseq,
#                     remove_pipe, Modelgenerator, modulos/script e algoritmos de filogenia 
# Usar o argumento  : Caminho do documento fasta de entrada + Documento x.fasta de entrada
#                     python profile_phylogeny_aa.py caminho_do_diretorio/file_multifasta.fasta
# (CASA)            : python myscript.py /home/kary/dir/d_06_casa/script/script_aa_pipeline/python/fasta/rh/rh.fasta
# (CASA ultima)     : python myscript.py /home/kary/dir/d_06_casa/script/script_aa_pipeline/python/fasta/rh
# ==============================================================================
# Data da ultima alteracao do script: 31/01/2008
#                                   : 07/01/2008
# ==============================================================================
#-------------------------------------------------------------------------------
# declarando os modulos a usar 
#-------------------------------------------------------------------------------
# 1. O modulo os tem logicamente relacao com seu sistema operacional
# 2. E o modulo commands logicamente tem relacao com os comandos deste sistema (seja qualquer um que rode Python) 
import os, sys, commands, shutil as sh
#-------------------------------------------------------------------------------
# Abrindo o diretorio: Trabalhando com o arquivo fasta
#-------------------------------------------------------------------------------
# dirin: diretroio do arquivo multifasta

def main(dirin):

	sys.setrecursionlimit(1000)

	for f in os.listdir(dirin):
		if f.endswith('.fasta'):
    			path_fasta = os.path.join(dirin, f)
    			#os.chmod(path_fasta, 0755)  # Assume it's a file

	#-------------------------------------------------------------------------------
	# Executando Mafft
	#-------------------------------------------------------------------------------
	import makeMafft_aa 
	makeMafft_aa.paramModuleExecution(dirin)

	#-------------------------------------------------------------------------------
	# Trabalhando com o arquivo mafft
	#-------------------------------------------------------------------------------
	for m in os.listdir(dirin):
		if m.endswith('.mafft'):                                                    
    			path_mafft = os.path.join(dirin, m)
    			os.chmod(path_mafft, 0755)  # Assume it's a file

	#-------------------------------------------------------------------------------
	# Corregindo Mafft e removendo pipes
	#-------------------------------------------------------------------------------
	import makeRemovePipe_aa 
	corrected_file = makeRemovePipe_aa.paramModule(path_mafft)

	#-------------------------------------------------------------------------------
	# Executando Readseq
	#-------------------------------------------------------------------------------
	import makeReadseq_aa
	makeReadseq_aa.paramModuleReadseq(path_mafft)

	#-------------------------------------------------------------------------------
	# Executando Modelgenerator
	#-------------------------------------------------------------------------------
	import makeModelgenerator_aa
	#makeModelgenerator_aa.paramModuleModelgenerator(dirin, path_mafft)
	#print "IMPORTED: The evolutionary model found is: " + makeModelgenerator_aa.paramModuleModelgenerator(dirin, path_mafft)
	param_model_evol = makeModelgenerator_aa.paramModuleModelgenerator(dirin, path_mafft)

	#-------------------------------------------------------------------------------
	# Executando Algoritmos Filogeneticos 
	#-------------------------------------------------------------------------------
	#-------------------------------------------------------------------------------
	#   3.- Executando PaupNJ
	#-------------------------------------------------------------------------------
	#import makePaupNJ_aa
	#makePaupNJ_aa.ModulePaupNJ(dirin, path_mafft)

	#-------------------------------------------------------------------------------
	#   7.- Executando RAxML
	#-------------------------------------------------------------------------------
	#import makeRaxml_aa
	#makeRaxml_aa.ModuleRaxml(dirin, param_model_evol)

	#-------------------------------------------------------------------------------
	#   5.- Executando Weighbor VER ERRO DO USO DO L
	#-------------------------------------------------------------------------------
	#import makeWeighbor_aa
	#makeWeighbor_aa.ModuleWeighbor(dirin, param_model_evol)

	#-------------------------------------------------------------------------------
	#   1.- Executando MrBayes
	#-------------------------------------------------------------------------------
	#import makeMrBayes_aa
	#makeMrBayes_aa.ModuleMrBayes(dirin, param_model_evol)

	#-------------------------------------------------------------------------------
	#   2.- Executando PaupMP
	#-------------------------------------------------------------------------------
	#import makePaupMP_aa
	#makePaupMP_aa.ModulePaupMP(dirin, path_mafft)

	#-------------------------------------------------------------------------------
	#   4.- Executando Phyml
	#-------------------------------------------------------------------------------
	import makePhyml_aa 
	makePhyml_aa.ModulePhyml(dirin, param_model_evol) 
	
	#-------------------------------------------------------------------------------
	#   6.- Executando Filogenia de Perfis
	#-------------------------------------------------------------------------------
	##Ainda em proceso falta concatenar
	#&makeFilogeniaPerfis($dirin)                 

	#-------------------------------------------------------------------------------
	#   X.- Executando Paml
	#-------------------------------------------------------------------------------
	###import makePaml_aa
	###makePaml_aa.ParamModulePaml(dirin, param_model_evol)


  
  
