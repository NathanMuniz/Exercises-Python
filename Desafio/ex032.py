a = int(input('Digite o primeito numero'))
b = int(input('Digite o segundo numero'))
c = int(input('Digite o Terceiro numero'))
menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c
# Omair
maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c
print('O menor É O {}'.format(menor))
print('e o mair é o {}'.format(maior))
