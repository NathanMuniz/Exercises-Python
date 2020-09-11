def cal(lar, com):
    area = lar * com
    print(f" A era de um terreno de {lar:.1f}X{com:.1f} é de {area:.1f}")


print("   Controle de Terrenos")
print(20 * "-")


larg = float(input("LARGURA (m): "))
comp = float(input("COMPRIMENTO (m): "))
cal(larg, comp)

