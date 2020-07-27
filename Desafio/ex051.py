print('Digite 10 termos de uma PA')
a1 = int(input('Primeiro Termo'))
r = int(input('Rasão'))
d = a1 + (10 - 1) * r
for c in range(a1, d + r, r):
    print('{}'.format(c), end= ' > ')
print('ACABO')
