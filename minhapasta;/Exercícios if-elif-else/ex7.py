idade = int(input("Digite a sua idade: "))
cnh = input("Tem CNH? (sim ou não): ")

if idade>=18 and cnh=="sim":
    print("Você é permitido a dirigir.")
elif idade>=18 and cnh=="não":
    print("Você tem o direito em colicitar a CNH, mas não pode dirigir.")
else:
    print("Você não tem idade para dirigir.")

    if idade>18:
        if cnh=="sim":
            print("Você é permitido a dirigir.")
        else:
            print("Você tem o direito em colicitar a CNH, mas não pode dirigir.")
    else:
        print("Você não tem idade para dirigir.")