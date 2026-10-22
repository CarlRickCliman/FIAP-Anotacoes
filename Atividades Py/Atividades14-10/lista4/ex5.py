while True:
    n1 = int(input("Digite um número: "))
    n2 = int(input("Digite outro número: "))

    if n1 != n2:
        print(n1+n2)
        break
    elif n1 == n2:
        print("Digite números distintos")
        continue
