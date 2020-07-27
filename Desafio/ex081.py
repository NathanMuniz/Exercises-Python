r = 'S'
lista = list()
while r != 'N':
    n = int(input('Digite um valor:'))
    lista.append(n)
    r = str(input('Quer Continuar? [S/N]')).upper()
print('-=' * 30)
print(f'Você Digitou {len(lista)} Elmentos')
lista.sort(reverse=True)
print(f'Os valores em ordem decrescente são: {lista}')
if lista.__contains__(5) == True:
    print('O valor 5 Faz Parte da lista')
else:
    print('O valor 5 não faz parte da lista')
