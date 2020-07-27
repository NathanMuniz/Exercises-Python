med1 = float(input('Primeira Nota'))
med2 = float(input('Segunda Nota'))
media = (med1 + med2)/2
print('Tirando {} e {}, A media do aluno è {} '.format(med1, med2, media))
if media < 5:
    print('Você foi REPROVADO')
elif media == 5 or media > 5 and media < 6.9:
    print('Você esta de RECUPERAÇÂO')
elif media == 7 or media > 7:
    print('Você esta APROVADO')
else:
    print('Erro')
print('Fim')



