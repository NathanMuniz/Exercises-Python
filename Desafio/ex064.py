n = 0
soma = 0
q = 0
n = int(input('Digite um Numero [999 Para parar]'))
while n != 999:
    soma = n + soma
    q = q + 1
    n = int(input('Digite um Numero [999 Para parar]'))
print('Você Digitou {} Numeros E a Soma deu {}'.format(q, soma))