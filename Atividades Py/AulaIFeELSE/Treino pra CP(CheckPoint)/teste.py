classe = str(input("Digite sua classe(media, baixa, alta): "))
idade = int(input("Digite sua idade (0 à 100): "))

if idade >= 18:
    if classe == "baixa":
        print("Vai arranjar um emprego.")
    elif classe == "media":
        print("Vai fazer uma faculdade e depois arranjar um emprego.")
    else:
        print("Herdeiro, nao precisa trabalhar, assume o negócio da sua familia.")
elif idade <18:
    if classe == "baixa":
        print("Finalize os estudos e vai arranjar um emprego.")
    elif classe == "media":
        print("Finalize os estudos e vai arranjar uma faculdade.")
    else:
        print("Nem precisa estudar, ja esta com a vida resolvida mesmo.")
else:
    print("Dados inválidos")


