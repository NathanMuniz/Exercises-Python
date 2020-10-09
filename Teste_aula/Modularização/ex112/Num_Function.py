def metade(n, format_moeda=True):
    meta = n / 2
    if format_moeda:
        return moeda(meta)
    else:
        return meta

def dobro(n, format_moeda=True):
    d = n * 2
    return moeda(d)


def aumentar(n, format_moeda=True, aumen=0):
    a = (n * aumen) / 100
    aumento = n + a
    return moeda(aumento)


def moeda(preco):
    moeda = "R$"
    return f"{moeda}{preco:.2f}".replace("." , ",")


def reduzir(n, dim):
    a = (n * dim) / 100
    r = n - a
    return moeda(r)


def resumo(preco, aumento=0, baixa=0):
    print(30 * "-")
    print(f"RESUMO DO VALOR".center(30))
    print(30 * "-")
    print(f"Preço analisado: \t {moeda(preco)}")
    print(f"Dobro do preço: \t {dobro(preco)}")
    print(f"Metade do preco: \t {metade(preco)}")
    print(f"{aumento}% de aumento: \t {aumentar(preco, aumen=aumento)}")
    print(f"{baixa}% de redução: \t {reduzir(preco, baixa)}")
    print(30 * "-")


def validar(sms):
    preco = str(input(f"{sms}"))
    preco = preco.replace("," , ".")
    while is_a_number(preco) != True:
        print(f'ERRO: "{preco.strip()}" é um preço inválido')
        preco = input(f"{sms}")
    return float(preco)


def is_a_number(n):
    n = n.replace("." , "")
    n = n.replace("," , "")
    n = n.replace(" ", "")
    if n.isnumeric() :
        return True
    else :
        return False