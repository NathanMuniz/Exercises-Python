
Valor = list()
while True:
    n = int(input('Digite um valor: '))
    if n not in Valor:
        Valor.append(n)
    else:
        print("Valor Duplicado não vou add... ")
    rep = str(input("Quer continuar?[S/N] ")).upper()
    if rep == "N":
        break
print(20 * "-=")
Valor.sort()
print(f"Você digitou os valores {Valor}")