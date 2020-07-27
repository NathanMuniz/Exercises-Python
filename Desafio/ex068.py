from random import randint
print('-='*20)
print('Vamoas Jogar Par ou Impar')
print('-='*20)
v = 0
while True:
    n = int(input('Digite um Valor :'))
    p = str(input('Par ou Impar [P/I]')).upper()
    c = randint(1, 10)
    r = ''
    soma = n + c
    if soma % 2 == 0:
        r = 'PAR'
    else:
        r = 'IMPAR'
    print('-='*20)
    print(f'Você Jogou {n} e o Computador jogou {c}, Total deu {soma} Deu {r} ')
    print('-='*20)
    if r == 'PAR' and p == 'P' or r == 'IMPAR' and p == 'I':
        v = v + 1
        print('Você Venceu, '
              'VAMOS Jogar novamente...')
    else:
        print('Você Perdeu ')
        print(f'Game Over ! VocÊ Venceu {v} Vezes ')
        break


