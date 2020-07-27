menor = 0
maior = 0
for c in range(1, 5):
    pes = int(input('Em Que Ano a \033[35m{}\033[m Pessoa Nasceu?'.format(c)))
    if pes >= 1999:
        menor = menor + 1
    else:
        maior = maior + 1
print('A \033[35m {}\033[m menor de idade e \033[36m{}\033[m maior de idade'.format(menor, maior))

