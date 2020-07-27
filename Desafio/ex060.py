#n = int(input('Dgite um numero '))
#c = n
#f = 1
#while c > 0 :
#    print('{}'.format(c), end='')
#    print('x'if c > 1 else '=', end='')
#    f = f * c
#    c = c-1
#print('O fatorial de {} é '.format(n))

n = int(input('Dgite um numero '))
c = n
f = 1
for g in range(c, -1, -1):
    print('{}'.format(c), end='')
    print('x'if c > 1 else '=', end='')
    f = f * c
    c = c-1
print('{}'.format(f))
