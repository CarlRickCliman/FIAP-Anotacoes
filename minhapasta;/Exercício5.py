salarioBase = float(1800)
comissao = float(150)
adicional = float(0.03)

nome = input('Digite seu nome: ')

quantidadeVendida = int(input('Digite a quantidade de produtos vendidos: '))

valorDasVendas = float(input("Digite o valor total das vendas: "))

salarioFinal = salarioBase+(quantidadeVendida*comissao)+(adicional*valorDasVendas)

print(f'Salário Final = {salarioFinal}')
