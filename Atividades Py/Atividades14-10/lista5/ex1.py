dia = input("Digite o dia da semana: ").lower()

match dia:
    case "segunda" | "terça" | "quarta" | "quinta" | "sexta":
        print("Dia útil")
    case "sábado" | "domingo":
        print("Final de semana!!")
    case _:
        print("Dia inválido...")