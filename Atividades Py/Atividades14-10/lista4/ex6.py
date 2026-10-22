menornumero = 0
for i in range(1, 11):
    n = int(input(f"[{i}] Digite um número: "))

    if menornumero == 0:
        menornumero = n
    elif n < menornumero:
        menornumero = n

print(menornumero)