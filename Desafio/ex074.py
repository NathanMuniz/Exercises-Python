from random import randint
numeros = (randint(1, 10), randint(1, 10), randint(1, 10),
     randint(1, 10), randint(1, 10))
print(' OS valores Sorteados Foram', end=' ')
for n in numeros:
    print(f'{n}', end=' ')
print(f'\nO maior Foi {max(numeros)}')
print(f'O menor foi {min(numeros)}')
