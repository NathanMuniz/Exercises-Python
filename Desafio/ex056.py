mediaidade = 0
somaidae = 0
maioridadehomem = 0
nomemaisvelho = ''
mulheresidade = 0
for p in range(1, 5):
    print('----- {} PESSOA -----'.format(p))
    nome = str(input('Nome')).strip()
    idade = int(input('Idade'))
    sexo = str(input('Sexo [M/F]:')).strip()
    somaidae += idade
    if p == 1 and sexo in 'Mn':
        nomemaisvelho = nome
    if sexo in 'Mn' and idade > maioridadehomem:
        maioridadehomem = idade
        nomemaisvelho = nome
    if idade <= 20  and sexo  in 'Ff':
        mulheresidade += 1
mediaidade = somaidae / 4
print('A media da idade do grupo é de {} anos'.format(mediaidade))
print('O nome so mais velho tem {} anos e se chama {}'.format(maioridadehomem, nomemaisvelho))

