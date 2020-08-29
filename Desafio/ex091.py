from time import sleep
from random import randint
from operator import itemgetter
jogo = {'jogador1': randint(1, 6),
        'jogador2': randint(1, 6),
        'jogador3': randint(1, 6),
        'jogador4': randint(1, 6)}
raking = dict()
for k, v in jogo.items():
    print(f"O {k} Tirou {v} no dado")
    sleep(1)
raking = sorted(jogo.items(), key=itemgetter(1), reverse=True)
print("-=" * 20)
print(" == RANKING DOS JOGADORES")
cont = 1
for k in (raking):
    print(f" {cont}°Lugar: {k[0]} com {k[1]} ")
    cont += 1