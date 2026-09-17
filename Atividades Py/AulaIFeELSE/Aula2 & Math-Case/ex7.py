idade = int(input("Digite a sua idade: "))
cnh = input("Tem CNH(sim ou não?:")

if idade<0:
    print("Idade inválida")
elif idade >= 18 and cnh=="sim":
    print("Permitido a dirigir")
elif idade>=18 and cnh=="não":
    print("Solicite a CNH para ser permitido a dirigir")
elif idade<18 and cnh=="não":
    print("Não é permitido a dirigir")
elif idade<18 and cnh=="sim":
    print("Você não tem idade suficiente para ter uma CNH definitiva")
else:
    print("Valores inválidos")
