print('----------------LOJAS Natbiel--------------------')
compra = float(input('Valor da compra'))
escolha = int(input('''Escolha a Forma de Pagamento 
(1) Dinheiro Ou Cheque
(2) Avista no Cartão 
(3) 2x no Cartão 
(4) 3X Ou mais no Cartão
'''))
if escolha == 1:
    print('Sua compra de R${:.2f} vai custar R${:.2f} no final'.format(compra, compra - (compra * 10)/ 100  ))
elif escolha == 2:
    print('Sua Compra de R${:.2f} Vai Custar R${:.2f} no final'.format(compra, compra - (compra * 5 )/ 100 ))
elif escolha == 3 or 4:
    esolha2 = int(input('Qunatas Veses Parcelado?'))
    if esolha2 <= 2:
        print('Sua Compra de R${:.2f} Vai Custar R${:.2f} no final'.format(compra, compra))
    else:
        print('Sua Compra de R${:.2f} Vai Custar R${:.2f} no final'.format(compra, compra + (compra * 20)/ 100))
else:
    print('Erro Tente Novamente')


