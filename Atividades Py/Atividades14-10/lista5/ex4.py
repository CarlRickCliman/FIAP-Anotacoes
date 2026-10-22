while True:

    numero = int(input("Digite um número inteiro: "))

    print("\n1 - O dobro \n2 - A metade \n3 - 10% do número")
    selecao = int(input("\n--- Digite a opção a ser realizada ---\n"))

    if selecao == 1:
        print(f"O dobro de {numero} é {numero * 2}")
        break
    elif selecao == 2:
        print(f"A metade de {numero} é {numero/2}")
        break
    elif selecao == 3:
        print(f"10% de {numero} equivale a {numero * 10 / 100}")
        break
    else:
        print("\nOpção inválida!\n")
        continue


