
print('Gerar Pa')
print('-=' *10)
first = int(input('Primeiro Termo'))
reason = int(input('Rasão da PA'))
term = first
total = 0
more = 10
cont = 1
while more != 0:
    total = total + more
    while cont <= total:
        print('{}'.format(term), end='')
        print(' → ', end='')
        term = term + reason
        cont = cont + 1
    more = int(input('Você quer Colocar Mais quantos  Termos ? '))