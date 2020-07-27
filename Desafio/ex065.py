
r = 'S'
soma = 0
term = 0
menor = 0
maior = 0
while r == 'S' :
    n = int(input('Digite um valor : '))
    soma = soma + n
    term = term + 1
    r = str(input('Quer continuar ? [S,N]')).strip().upper()
    if n > maior:
        maior = n
    elif n < menor:
        menor = n
media = soma / term
print('A soma foi {} e você digitou {} Numeros'.format(soma, term))
print('A media foi {} e o maior foi {}e o manor foi {} '.format(media, maior, menor))