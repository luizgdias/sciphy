import os, time

# x = os.listdir('inputTestGc')
# with open('lista.txt', 'w') as f:
#     for item in x:
#         f.write("%s_\n" % item)

# txt = "isso#e#um"
# x = txt.split("#")
# print(x)

# ref_arquivo = open("lista.txt","r")
# lista_de_linhas = ref_arquivo.readlines()
# print(len(lista_de_linhas))

controle = False

while(controle == False):
	for i in range(0, 11):
   		print(i)
   		time.sleep(5)
		controle = True