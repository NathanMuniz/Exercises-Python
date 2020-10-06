import Num_Function as nf

n = float(input("Digite o preço R$ "))
print(f"A metade de {n:.2f} é R${nf.metade(n):.2f} ")
print(f"O Dobro de {n:.2f} é R${nf.dobro(n):.2f}")
print(f"Aumentando 10%, temosR$ {nf.aumentar(n):.2f}")
