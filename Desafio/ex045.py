from random import randint
itens = ('pedra','pepel','tesoura')
computador = randint(0, 2)
print('''Suas opçoês 
[ 0 ] pedra
[ 1 ] papel
[ 2 ] tesoura ''')
jogador = int(input('Qual sua jogada?'))
print('Computador jogou {}'.format(itens[computador]))
print('jogador jogou {}'.format(itens[jogador]))
if computador == 0:
    if jogador == 0:
        print('EMPATE')
    elif jogador == 1:
        print('O JOGADOR VENCEU')
    elif jogador == 2:
        print('O COMPUTADOR VENCEU')
    else:
        print('ERRO DE NALISE')
elif computador == 1:
    if jogador == 0:
        print('O COMPUTADRO VENCEU')
    elif jogador == 1:
        print('EMPATE')
    elif jogador == 2:
        print('O JOGADOR VENCEU')
    else:
        print('ERRO DE NALSE')
elif computador == 2:
    if jogador == 0:
        print('O JOGADOR VENCEU')
    elif jogador == 1:
        print('O COMPUTADOR VENCEU')
    elif jogador == 2:
        print('EMPATE')
    else:
        print('ERRO DE ANALISE')
print('Fim')