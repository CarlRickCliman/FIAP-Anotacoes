# ------------------------------------------------------------
# |Match-Case 1 -- Compara valores de igualdade.                |
# |(match -variável-                                          |
# | case1:                                                    |
# |     print()                                               |
# | case2:                                                    |
# |    print()                                                |
# ------------------------------------------------------------

opcao = int(input("Digite uma opção(0 à 3): "))

match opcao:
    case 0:
        print("Opção 0")
    case 1:
        print("Opção 1")
    case 2:
        print("Opção 2")
    case 3:
        print("Opção 3")
    case _:
        print("Valor incorreto. Digite de 0 até 3.")


#ou

if opcao == 0:
    print("Opção 0")
elif opcao == 1:
    print("Opcao 1")
elif opcao ==2:
    print("Opção 2")
elif opcao == 3:
    print("Opção 3")
else:
    print("Valor incorreto. Digite de 0 até 3.")