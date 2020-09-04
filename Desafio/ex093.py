# Ler dados do Jogador
jogador = dict()
jogador["nome"] = str(input("Nome do Jogador: "))
part = int(input(f"Quantas partidas {jogador['nome']} jogou?"))
total = 0
gols = list()
for c in range(0, part):
    gol = int(input(f"    Quantos gols na partida {c}: "))
    total = gol + total
    gols.append(gol)
jogador["goal"] = gols
jogador["total"] = total

# Mostra forma Dicionário
print(20*"-=")
print(jogador)

# Mostrar forma k v
print(20*"-=")
for k,v in jogador.items():
    print(f"O campo {k} tem o valor {v}")

# Mostrar forma "difícil"
print(20*"-=")
print(f"O jogador {jogador['nome']} jogou {part} partidas.")
for c, v in enumerate(gols):
    print(f"   => Na partida {c}, fez {v}")
print(f"Foi um total de {len(gols)}")
print()