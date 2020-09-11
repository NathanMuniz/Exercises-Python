jogador = dict()
jogadores = list()
run = True
goals = list()
total = 0
# Ler os dados dos jogadores 
while run: 
    jogador.clear()
    # Ler nome   
    jogador["nome"] = str(input("Nome do jogador: "))
    # Ler Total de paridas
    part = int(input(f"Quantas partidas o {jogador['nome']} jogou: "))
    # Ler quantos goals marcou em cada partida
    for p in range(0, part):
        gol = int(input(f"    Quantos gols marcou na {p + 1} partida "))
        total += gol
        goals.append(gol)
    # Adicionar a uma lista cada jogador
    jogador["goal"] = goals[:] 
    goals.clear()
    jogador["total"] = total
    total = 0   
    jogadores.append(jogador.copy())

    # Quer continuar 
    while True:
        resp = str(input("Quer contrinuar [S/N]: ")).upper()[0]  
        if resp in "SN":
            break
        print("[ERRO] respnda apenas S ou N")
    if resp == "N":
        run = False


# Mostra Dados

# Fazer cabeçalho
print(30 * "-=")
print('cod ', end="")
for i in jogador.keys():
    print(f"{i:<15}", end="")
print()

# Mostrar dados
print(30 * "-")
for k, v in enumerate(jogadores):
    print(f"{k:>3}", end="")
    for d in v.values():
        print(f" {str(d):<15}", end="")
    print()
print("-" * 40)

# Mostrar Dados de jogadores Específicos
while True:
    resp = int(input("Mostar dados de qual jogador [999 para parar]: "))
    if resp == 999:
        break
    elif resp >= len(jogadores):
        print(f"[ERRO] não existe jogador com o código {resp}")
    else:
        print(f"-- LEVANTAMENTO DO JOGADOR {jogadores[resp]['nome']}")
        for k, v in enumerate(jogadores[resp]['goal']):
            print(f"    No jogo {k + 1} fez {v}")
    print(40 * "-")
print("<< VOLTE SEMPRE >>") 
