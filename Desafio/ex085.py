num = [[], []]
valor = 0
for c in range(1, 8):
    valor = int(input(f"Digite o {c}° Valor"))
    if valor % 2 == 0:
        num[0].append(valor)
    else:
        num[1].append(valor)
print(20 * "-=")
num[0].sort()
num[1].sort()
print(f"Os valores Pares foram {num[0]}")
print(f"os valores Imapres Foram {num[1]}")