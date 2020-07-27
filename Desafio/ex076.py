Listagem = 'Lápis',1.7, 'Borracha',2,'Caderno',15.90,'Estojo',25,'Tranferidor',4.20,'Compasso',9.99


print('-'*20)
print('Lista de Preços')
print('-'*20)
for iten in range(0, len(Listagem, )):
    if iten % 2 == 0:
        print('Eu Comprei Um ', end='')
        print(f'{Listagem[iten]:.<30}', end='')
    else:
        print(f'Preço R$: {Listagem[iten]:.2f}')