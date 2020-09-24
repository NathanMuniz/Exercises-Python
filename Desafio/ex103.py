def jogador(n="<desconhecido>", g = 0):
    return f"O jogador {n} fez {g} gol(s) no  campeonato."


print(30 * "-")
nome = str(input("Nome do jogador: "))
goal = input("Número de gols: ")

if nome == "" and goal == "" : 
    print(jogador())
elif nome == "":
    print(jogador(g=goal))
elif goal == "":
    print(jogador(n=nome))
else:
    print(jogador(nome, goal))

