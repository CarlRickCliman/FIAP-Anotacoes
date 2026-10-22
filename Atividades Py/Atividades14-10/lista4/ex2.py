pessoas = 0
menordeidade = 0
while pessoas < 10:
    pessoas += 1
    idade = int(input(f'{pessoas} Digite a sua idade: '))
    if idade < 18:
        menordeidade += 1


print(f"Total de pessoas menores que 18: {menordeidade}")

