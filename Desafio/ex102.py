def fatorial(num, show=False):
    f = 1
    for c in range(num, 0, -1):
        if show:
            print(f"{c}", end=" ")
            if c > 1:
                print(" X ", end=" ")
            else:
                print(f" = ", end="")
        f *= c
    return f

print(fatorial(5, False))