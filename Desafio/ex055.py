maior = 0
menor = 0
for c in range(1, 6):
    pes = float(input('o pess da \033[31m{}\033[m Pessoa '.format(c)))
    if maior <= pes:
        maior = pes
    if pes >= maior:
        menor = pes
print(maior)
print(menor)
