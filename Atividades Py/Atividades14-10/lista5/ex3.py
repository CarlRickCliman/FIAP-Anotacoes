mes = input("Ditgite o nome de um mês do ano: ").lower()

match mes:
    case "dezembro" | "janeiro" | "fevereiro":
        print("Verão")
    case "março" | "abril" | "maio":
        print("Outono")
    case "junho" | "julho" | "agosto":
        print("Inverno")
    case "setembro" | "outubro" | "novembro":
        print("Primavera")
    case _:
        print("Mês inválido!!")
