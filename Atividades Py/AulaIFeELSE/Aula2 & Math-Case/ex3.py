dia = int(input("Digite o dia da semana(1 à 7): "))

match dia:
    case 7 | 1:
        print("Final de Semana, dias de farra")
    case 2 | 3 | 4 | 5 | 6:
        print("Dia útil, vai trabalhar vagabundo")