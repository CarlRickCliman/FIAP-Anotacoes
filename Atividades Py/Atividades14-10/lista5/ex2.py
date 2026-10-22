valor = float(input("Digite um valor: R$"))
sigla = input("Digite a sigla da moeda que gostaria de converter: ").lower()
match sigla:
    case "usd" | "dólar" | "dolar":
        valor *= 0.20
        print(f"Valor convertido em dólar: {valor}")
    case "eur" | "euro":
        valor *= 0.18
        print(f"Valor convertido em dólar: {valor}")
    case "gbp" | "libra":
        valor *= 0.15
        print(f"Valor convertido em dólar: {valor}")
    case _:
        print("Moeda não suportada")