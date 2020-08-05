matrix = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
par = pars = col = colSoma = mai = maiValor = 0

# Criar Matrix
for l in range(0, 3):
    for c in range(0, 3):
        matrix[l][c] = (int(input(f"Digite um número para a posição [{l}] [{c}]: ")))

         #Soma dos Valores pares 
        if matrix[l][c] % 2 == 0:
            par = matrix[l][c]
            pars = par + pars 

# Imprimir Matrix
for l in range(0, 3):
    for c in range(0, 3):
        print(f"[{matrix[l][c]}]", end="")
    print()

# Soma dos valores da 3° Coluna 
for f in range(0, 3):
    col = matrix[f][2]
    colSoma = col + colSoma

 #  Coluna e quem é o maior da 2° linha   
    mai = matrix[1][f]
    if mai >= maiValor:
        maiValor = mai




print(f"\n A soma dos valores pares é {pars}.")
print(f"A soma dos valores da terceira coluna é {colSoma}.")
print(f"O maior valor da sugunda linha é {maiValor}.")
