pessoa = dict()
while True:
    nome = str(input("Nome: "))
    media = float(input(f"Média de {nome}: "))
    pessoa = {"media" : media}
    pessoa["nome"] = nome
    pessoa["situcao"] = "empty"
    if media < 7 and media >= 5:
        pessoa["situacao"] = "Recuperação"
    elif media < 5:
        pessoa["situcao"] = "Reprovado"
    else:
        pessoa["situacao"] = "Aprovado"
    print(20 * "-=")
    for k, v in pessoa.items():
        print(f"{k} é igual a {v}")
    res = str(input("Quer Continuar [S/N]")).upper
    if res == "N":
        break
print()