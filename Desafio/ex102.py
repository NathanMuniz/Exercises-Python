def fatorial(num, show=False):
    fato = num
    for c in range(1, num):
        if show:
            print(f"{c} x", end=" ")
        fato = fato * c
    return fato
    

print(fatorial(5, True))
