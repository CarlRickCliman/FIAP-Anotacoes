while True:
    print("Sistema de Reservas")
    print("\n1. Check-in")
    print("2. Check-out")
    print("3. Consultar Quarto")
    print("4. Sair")

    opcao = int(input("\nEscolha uma opção: "))

    match opcao:
        case 1:
            print("\nCheck-in realizado com sucesso!")
        case 2:
            print("\nCheck-out realizado com sucesso!")
        case 3:
            quarto = input("\nDigite o número do quarto: ")
            print(f"Consultando quarto {quarto}...")
            print(f"\nQuarto {quarto} disponível!!!\n")
        case 4:
            print("\nSaindo do sistema...")
            break
        case _:
            print("\nOpção inválida!")
            continue