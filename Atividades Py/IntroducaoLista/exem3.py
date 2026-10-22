# LISTA COM REPETIÇÃO
veiculos = ['Gol', 'Kwid', 'HB20', 'UP', 'Mobi']
# Acesso posicional
#For-each
#for item in nome_da_lista:
print("Percorrendo uma lista com for-each")
i = 0 #index

#item é uma variável local, criada para receber 1 valor da lista a cada loop
for item in veiculos:
    print(f"{i} : {item}")
    i+=1

#Obter o tamanho da lista
print("O tamanho da lista é: ", len(veiculos))


# OU
# For
#for i in range(len(lista)
print("Percorrendo uma lista com for ")
# for necessita da variável i para percorrer na lista
for i in range(len(veiculos)):
    print(f"{i} : {veiculos[i]}")
    #i: index


#OU
#While i < len(lista):
ii = 0
print("\nPercorrendo uma lista com While\n")
while ii< len(veiculos):
    print(f"{ii} : {veiculos[ii]}")
    ii+=1