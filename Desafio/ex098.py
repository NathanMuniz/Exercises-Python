from time import sleep


def contar(inicio, fim, passo):
      if passo < 0:
        passo *= -1
    if passo == 0:
        passo = 1
    print(40 * "-=")
    print(f"Contagem de  {inicio} até o {fim} de {passo} em {passo}")
    sleep(2)
    if inicio < fim:
        for c in range(inicio, fim + 1, passo):
            print(c, end=" ", flush=True)
            sleep(0.5)
        print("FIM!")
    else:
        for c in range(inicio, fim, -passo):
            print(c, end=" ", flush=True)
            sleep(0.5)
        print("FIM!")

contar(1, 10, 2)
contar(10, 0, 1)
print("Agora é a sua vez de personalizar a contagem! ")
contar(int(input("Incio: ")), int(input("Fim: ")), int(input("Passo: ")))
