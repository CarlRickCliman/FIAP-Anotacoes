intervalo = 0

for i in range(1, 16):
    n = int(input(f"[{i}] Digite um número: "))

    if 50 > n > 10:
        intervalo += 1

print(f"Há {intervalo} números entre 10 e 50")