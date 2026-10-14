salario = float(input("Digite seu salário atual: "))
percentual = float(input("Digite o percentual de reajuste(Somente o número): "))

salarioAtualizado = salario + (salario * (percentual/100))

print(f"Seu novo salário é {salarioAtualizado}")