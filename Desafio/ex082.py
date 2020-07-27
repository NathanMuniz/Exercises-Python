lista = list()
impar = list()
par = list()
while True:
    n = int(input('Digite um numero: '))
    lista.append(n)
    if n % 2 == 0:
        par.append(n)
    else:
        impar.append(n)
    r = str(input('Quer continuar ? [S/N]'))
    if r in 'Nn':
        break
print('-=' * 30)
print(f'A lista completa é {lista}')
print(f'A lista de pares é {par}')
print(f'A lista de impar é {impar}')


