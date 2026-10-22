valores = int(input("Digite a quantidade de valores a serem lidos: "))
pares = 0
impares = 0
somapares = 0
somaimpares = 0
for n in range(1, valores + 1):
    print(n)
    if n % 2 == 0:
        somapares += n
        pares += 1
    else:
        somaimpares += n
        impares += 1

print(f"Quantidade de números pares: {pares}")
print(f"Média dos números pares: {somapares/pares}")
print("\n-------------------------------------------------\n")
print(f"Quantidade de números impares: {impares}")
print(f"Média dos números impares: {somaimpares/impares}")