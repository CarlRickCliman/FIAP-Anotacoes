# ------------------------------------------------------------
# |Match-Case 2 -- Compara valores de igualdade.                |
# |(match -variável-                                          |
# | case1:                                                    |
# |     print()                                               |
# | case2:                                                    |
# |    print()                                                |
# ------------------------------------------------------------
from unittest import case

dia = int(input("Digite o dia da semana(1 à 7): "))

match dia:
    case 1:
        print("Domingo")
    case 2:
        print("Segunda")
    case 3:
        print("Terça")
    case 4:
        print("Quarta")
    case 5:
        print("Quinta")
    case 6:
        print("Sexta")
    case 7:
        print("Sábado")
    case _:
        print("DIa inválido!")