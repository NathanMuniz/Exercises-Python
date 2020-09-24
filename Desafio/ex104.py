
def leiaInt(inp):
    ok = False
    while True:
        n = str(input(inp))
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print("[Erro]")
        if ok:
            break
    return valor


# Programa Principal
n = leiaInt("Digite um númeoro: ")
print(f"Você acabou de digitar o número {n}")