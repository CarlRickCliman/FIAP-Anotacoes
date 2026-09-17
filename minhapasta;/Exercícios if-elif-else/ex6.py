senha = input("Digite a senha: ")
usuario = input("Digite o nome do Usuario: ")



if senha != "fiap" or usuario != "admin":
    print("Senha Ou Usuario incorreto")
else:
    print("Acesso permitido")


if senha == "fiap" and usuario == "admin":
    print("Acesso permitido")
else:
    print("Senha incorreta")
