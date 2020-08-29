from time import sleep
from datetime import date
data_atual = date.today()
data = data_atual.year
# Pegar os Dados principais
pessoa = dict()
pessoa["nome"] = str(input("Nome: "))
pessoa["idade"] = 2020 - int(input("Ano de Nacimeto: "))
pessoa["ctpt"] = int(input("Carteira de Trabalho (0 não tem): "))

# Se tiver Carteira de Trabalho 
if pessoa["ctpt"] != 0:
    pessoa["contra"] = int(input("Ano de Contratação: "))
    pessoa["salário"] = float(input("Salário: "))
    anos_de_trabalho = data - pessoa["contra"]
    pessoa["aposentadoria"] = (35 - anos_de_trabalho) + pessoa["idade"]

print(30 * "-=")

# Mostrar a kay e valor de cada assunto
for k, v in pessoa.items():
    print(f"  - {k} tem o valor {v}")
    sleep(1.5)

