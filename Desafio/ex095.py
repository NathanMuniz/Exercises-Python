jogador = dict()
jogadores = list()
run = True
goals = list()
total = 0
# Ler os dados dos jogadores 
while run: 
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
    jogador.clear()

    # Quer continuar 
    resp = str(input("Quer contrinuar [S/N]: ")).upper()
    if resp == "N":
        run = False

# Mostra Dados
print(20 * "-=")
print("cod nome      goals       total")
print(20 * "-")
