dia = input("Digite o dia da semana: ").lower()

#função lower: transformar texto em minúsculo
#OR no Match-Case é o | (pipe)
match dia:
    case "segunda" | "terça" | "quarta" | "quinta" | "sexta":
        print("Dia útil")
    case "sábado" | "domingo":
        print("Final de semana")
    case _:
        print("Dia inválido")


if (dia == "segunda"
        or dia == "terça"
        or dia == "quarta"
        or dia == "quinta"
        or dia == "sexta"):

    print("Dia útil")

elif dia == "sábado" or dia == "domingo":
    print("Final de semana")

else:
    print("Dia inválido")