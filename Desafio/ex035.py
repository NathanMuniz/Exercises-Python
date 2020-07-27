print('-='*20)
print('Analizador de triandulos')
print('-='*20)
a = float(input('Primeira reta'))
b = float(input('Segunda reta reta'))
c = float(input('Terceira reta'))
if a < b + c and b < a + c and c < a + b:
    print('Os seguimentos acima podem formar triandulo')
else:
    print('Os seguimentos acima não podem fromar triangulos')
