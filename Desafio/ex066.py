n = s = q =  0
while True:
    n = int(input('Digite Um Numero(999 para parar):'))
    if n == 999:
        break
    s = n + s
    q = q + 1
print(f'A soma dos {q} Valores foi {s}')
