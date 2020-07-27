total = caro = cont = menor =  0
while True:
    produto = str(input('Nome do Produto?:'))
    preço = float(input('Preço R$:'))
    cont += 1
    total = total + preço
    if preço > 1000:
        caro =+ 1
    if cont == 1:
        menor = preço
    else:
        if preço < menor:
            menor = preço
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer Contunuar ? [S/N]')).strip().upper()[0]
    if resp == 'N':
        break
print(f'O total da compra è:R${total:.2f}')
print(f'Temos {caro} Produtos custando mais de R$1000')
print(f'O Produto Mais barato é {menor}')