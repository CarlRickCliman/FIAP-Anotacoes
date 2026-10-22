#Lista dentro de lista (ou Matriz)

#Uma matriz 3x3 (3 Linhas e 3 Colunas)
matriz = [
    [1,2,3], #Linha 0
    [4,5,6], #Linha 1
    [7,8,9]  #Linha 2
]

# Acessar uma matriz

print(matriz[0][0])
print(matriz[1][2])

#
print("Percorrendo uma matriz")
for linha in matriz:
    for coluna in linha:
        print(coluna, end= " ")
    print()