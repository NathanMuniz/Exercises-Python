
def vota(ano):
    from datetime import date
    ano_atual = date.today().year
    global idade 
    idade = ano_atual - ano
    if idade >= 18 and idade <= 60:
        return "VOTO OBRIGATÓRIO"
    elif idade < 18 and idade > 15 or idade >= 60:
        return "VOTO OPOCIONAL"
    else:
        return "NÃO VOTA"



print("-" * 20)
ano = int(input("Em que ano você nasceu ? "))
sevota = vota(ano)
print(f"Com {idade} anos: {sevota}")