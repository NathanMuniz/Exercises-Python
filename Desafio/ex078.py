lista = list()
maior = 0
menor = 99999
for c in range(0, 5):
    lista.insert(c, int(input(f"Digite um valor para a posição {c}: ")))
    if lista[c] >= maior:
        maior = lista[c]
    if lista[c] <= menor:
        menor = lista[c]
print(f"Você digitou os calores {lista}")
print(f"O maior valor digitado foi {maior} nas posições ", end=" ")
for pos, c in enumerate(lista):
    if lista[pos] == maior:
        print(f"{pos}...", end=' ')
print(f"\nO menor valor foi {menor} nas Posições", end=" "),
for pos, c in enumerate(lista):
    if lista[pos] == menor:
        print(f"{pos}..." , end=" ")