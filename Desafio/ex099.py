from time import sleep


def analisar(*num):
    print(40 * "-=")
    mai = 0
    print("Analisando valores passados...")
    sleep(1)
    if num[0] == 0 and len(num) == 1:
        print("Foram informados 0 valores ao todo.")
        print("O maior valor informado foi 0")
    else:
        for v in num:
            if v >= mai:
                mai = v
            print(v, end=" ")
        print(f"Foram informados {len(num)} valores ao todo.")
        sleep(2)
        print(f"O mair valor informado foi {mai}.")
    sleep(2)


analisar(2, 9, 4, 5, 7, 1)
analisar(4, 7, 0)
analisar(1, 2)
analisar(6)
analisar(0)