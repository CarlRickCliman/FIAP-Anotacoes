idade = int(input("Digite a sua idade: "))
cnh = input("Tem CNH(sim ou não?:")

match idade,cnh:
    case x,y if x >=18 and y == "sim":
        print("Permitido a dirigir")
    case x,y if x < 18 and y == "não":
        print("Não é permitido a dirigir")
    case x,y if x>=18 and y == "não":
        print("Solicite a CNH para dirigir")
    case _:
        print("Valores inválidos")

#ou

match idade,cnh:
    case x, "sim" if x >=18:
        print("Permitido a dirigir")
    case x, "não" if x < 18:
        print("Não é permitido a dirigir")
    case x, "não" if x>=18:
        print("Solicite a CNH para dirigir")
    case _:
        print("Valores inválidos")