num = int(input('Digite Um Numero '))
for c in range(1, num + 1):
    if num % c == 0:
        print('\033[33m', end= ' ')
    else:
        print('\033[31,', end= ' ')
    print('{}'.format(c), end= ' ')

