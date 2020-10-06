def metade(n):
    meta = n / 2
    return moeda(meta)


def dobro(n):
    d = n * 2
    return moeda(d)


def aumentar(n):
    a = (n * 10) / 100
    aumento = n + a
    return moeda(aumento)


def moeda(preco):
    moeda = "Rs"
    return f"{moeda}{preco:.2f}".replace("." , ",")