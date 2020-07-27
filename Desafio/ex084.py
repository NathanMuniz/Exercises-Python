pessoas = list()
pes = list()
quant = mai = 0
men = 9999


while True:
    pes.append(str(input("Nome: ")))
    pes.append(float(input("Peso: ")))

    # Menor e Maior Peso e Nome
    if pes[1] >= mai:
        mai = pes[1]
    elif pes[1] <= men:
        men = pes[1]

    # Adicionar na lista pessoas
    pessoas.append(pes[:])
    pes.clear()
    quant += 1

    # Parar loop
    r = str(input("Quer Continuar? [S/N]")).upper()
    if r == "N":
        break


print(20 * "=-")

print(f"Ao todo, você cadastrou {quant} pessoas ")

print(f"O maior peso foi de {mai}Kg. Peso de ", end=" ")
for p in pessoas:
    if p[1] == mai:
        print(p[0], end=" ")
print()

print(f"O menor peso foi de {men}. Peso de ", end=" ")
for p in pessoas:
    if pessoas == men:
        print(f" {p[0]}", end=" ")