horas = int(input("Digite a quantidade de horas(0 à 23): "))
minutos = int(input("Digite a quantidade de minutos(0 à 59): "))

if 0 < horas <= 23 and 0 < minutos <= 59:
    print(f"{horas}:{minutos}")
else:
    print("Horário inválido")