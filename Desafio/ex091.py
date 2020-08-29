from random import randint
from operator import itemgetter
from time import sleep
# Sortear dados para jogadores
jogadores = {"jogador1" : randint(1, 6),
             "jogador2" : randint(1, 6),
             "jogador3" : randint(1, 6),
             "jogador4" : randint(1, 6)}
for k, v in jogadores.items():
    print(f"{k} tirou {v} no dado")
print(30 * "-=")
sleep(1)

# Mostra ranking em ordem decrescente 
ranking = dict()
ranking = sorted(jogadores.items(), key=itemgetter(1), reverse=True)
print("  == RANKING DOS JOGADORES ==  ")
for k, v in enumerate(ranking):
    print(f"{k + 1}° lugar: {v[0]} com {v[1]}")
    sleep(1)
