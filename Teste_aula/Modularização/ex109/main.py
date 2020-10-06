import Num_Function as nf

n = float(input("Digite o preço R$ "))
print(f"A metade de {nf.moeda(n)} é {nf.metade(n)} ")
print(f"O Dobro de {nf.moeda(n)} é R${nf.dobro(n)}")
print(f"Aumentando 10%, temos {nf.aumentar(n)}")