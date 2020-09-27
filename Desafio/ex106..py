from time import sleep


def titulo(text, cor="nada"):
    if cor != "nada":
        print(f"{cor}" + (len(text) + 5) * "~")
        print(f"{text}")
        print((len(text) + 5) * "~" + "\033[m")


def ajuda(bio):
    titulo(f"Acessadno o manual do comando '{bio}'", "\033[1;104m")
    sleep(4)
    print("\033[1;106m")
    print(f"\033[1;30m{help(bio)}\033[m")
    print("\033[m")
    sleep(5)


run = True
while run:
    titulo("SISTEMA DE AJUDA PyHelp", "\033[1;102m")
    fun_analisar = str(input("Função ou Biblioteca > "))
    if fun_analisar.upper == "FIM":
        run = False
    else:
        ajuda(fun_analisar)