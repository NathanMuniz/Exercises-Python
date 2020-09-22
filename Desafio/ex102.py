def fatorial(num, show=False):
    fato = 1
    for c in range(num, 0, -1):
        if show:
            print(f"{c}", end="")
            if c > 1:
                print(" X ", end="")
            else:
                print(" = ", end="")
        fato *= c
    return fato
    

print(fatorial(5, False))
