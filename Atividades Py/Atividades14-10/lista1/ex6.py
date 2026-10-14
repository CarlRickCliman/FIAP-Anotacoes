salario = float(input("Digite seu salário fixo: "))
valordevendas = float(input("Digite o valor das vendas feitas no mês:"))

if valordevendas <= 5000:
    print(salario)
    print(f"Comissão Recebida: {valordevendas * 0.05}")
    salario += valordevendas * 0.05
    print(f"Salário total: {salario:.2f}")


