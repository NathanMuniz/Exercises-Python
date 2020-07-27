print('Gerar Pa')
print('-=' *10)
first = int(input('Primeiro Termo'))
reason = int(input('Rasão da PA'))
term = first
cont = 1
while cont <= 10:
    print('{}'.format(term), end='')
    print(' → 'if cont <= 9 else '', end='')
    term = term + reason
    cont = cont + 1

'''print('Gerar Pa')
print('-='*10)
first = int(input('Primeiro Termo'))
reason = int(input('Rasão sa PA'))
term = first
for c in range(10 , 0, -1):
    print('{}'.format(term), end='')
    print(' → 'if c <= 10 else '',end='')
    term = term + reason'''

