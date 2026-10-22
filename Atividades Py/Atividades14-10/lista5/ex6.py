
print("CÓDIGO   PRATO             VALOR\n"
      "1        Hamburguer        R$ 40,00\n"
      "2        Lasanha           R$ 60,00\n"
      "3        Bife acebolado    R$ 30,00\n"
      "4        Strogonoff        R$ 35,00\n"
      "5        Picanha           R$ 60,00\n"
      "6        Churrasco         R$ 60,00")

while True:
    codigo = int(input("\nDigite o código do prato: "))

    match codigo:
        case 1:
            prato = "Hamburguer"
            preco = 40.00
        case 2:
            prato = "Lasanha"
            preco = 60.00
        case 3:
            prato = "Bife acebolado"
            preco = 30.00
        case 4:
            prato = "Strogonoff"
            preco = 35.00
        case 5:
            prato = "Picanha"
            preco = 60.00
        case 6:
            prato = "Churrasco"
            preco = 60.00
        case _:
            print("Prato não encontrado")
            continue

    taxa = input("Deseja incluir a taxa de serviço de 10%? (Sim/Não): ").lower()

    if taxa == "sim":
        total = preco * 1.10
    else:
        total = preco

    print(f"Prato escolhido: {prato}")
    print(f"Valor total a pagar: R$ {total:.2f}")
    break