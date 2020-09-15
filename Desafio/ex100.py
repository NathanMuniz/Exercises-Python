from random import randint
from time import sleep
lista = list()


def sortear():
    print("Sorteando 5 Valores da lista: ", end="", flush=True)
    for c in range(0, 5):
        lista.append(randint(1, 10))
        sleep(1)
        print(lista[c], end=" ", flush=True)
    print("PRONTO!")


def somar():
    som = 0
    print(f"Somando os valores pares de {lista}, tesmos", end=" ")
    for v in lista:
        if v % 2 == 0:
            som = som + v
    print(som)


sortear()
somar()
