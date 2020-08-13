from random import randint
from time import sleep
print(20 * "-=")
print(10 * " " +  "JOGA NA MEGA SENA")
print(20 * "-=")
n = int(input("Quantos você quer que eu sortei ? "))
print(3 * "-=" + f"SORTEANDO {n} JOGOS " + 3 * "-=" )

lista = listaPrin =  list()
for jog in range(1, n + 1):
    listaPrin.append(lista[:])
    lista.clear()
    for c in range(0, 6):
        pc = randint(1, 60)
        if pc not in lista:
            lista.append(pc)
    listaPrin.sort
    print(f"Jogo {jog}: {listaPrin}")
    sleep(0.8)
print(20 * "-=" + " < BOA SORTE! >" + 20 * "-=")