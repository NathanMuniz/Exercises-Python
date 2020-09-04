pessoa = dict()
pessoas = list() 
som = 0
# pedir dados das pessoas
run = True
while run:
    # Nome
    pessoa["nome"] = str(input("Nome: "))

    # Verificar se sexo foi corretamente digitado
    while True:
        pessoa["sexo"] = str(input("Sexo: [M|F] ")).upper() 
        if pessoa["sexo"] not in "MF":
            print("[ERRO] Digite apena M ou F")
        else:
            break

    # Idade
    pessoa["idade"] = int(input("Idade: "))

    som += pessoa["idade"]
    pessoas.append(pessoa.copy())
    pessoa.clear()
    resp = ""
    # Veficar se quer continuar e analisar se foi corretamente digitado
    while resp != "S":
        resp = str(input("Quer continuar? [S|N]")).upper()
        if resp not in "SN":
            print("[ERRO] Responda apenas S ou N")
        elif resp == "N":
            run = False
            break

media = som / len(pessoas)
# Mostrar dados: Quantas pessoas e A média
print(30 * "-=")
print(f"A) Ao todo temos {len(pessoas)} pessoas cadatradas")
print(f"B) A Média da idadae é de {media:.2f} anos.")


# Mostrar mulheres cadastradas
print("C) As mulheres cadastradas foram ", end=" ")
for p in pessoas:
    if p["sexo"] == "F":
        print(f"{p['nome']}", end="")
        print()

# Mostrar pessoas acima da Média
print("Lista de pessoas que estão acima da média: ", end=" ")
for p in pessoas:
    if p["idade"] > media:
        print(f"\nnome = {p['nome']}; sexo = {p['sexo']}; idade = {p['idade']}")
