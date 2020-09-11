def tran_titulo(tit):
    x = len(tit)
    print((x + 5) * "~")
    print(f"   {tit}")
    print((x + 5) * "~")


titulo_principal = "Gustavo Guanabara"
titulo_secundario = "Curso de Python no Youtube"
paragrafo = "Cev"

tran_titulo(titulo_principal)
tran_titulo(titulo_secundario)
tran_titulo(paragrafo)