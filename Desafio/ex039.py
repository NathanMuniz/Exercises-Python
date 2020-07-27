from
atual = date.today().year
ano = int(input('Que Ano Voce nasceu:'))
idade = atual - ano
print('Quem nasceu em {} tem {} anos em {}'.format(ano, idade, atual))
if idade == 18:
    print('Você tem que se alistar IMEDIATAMENTE')
elif idade < 18:
    print('Falta {} Anos para Você se ALISTAR '.format(18 - idade))
elif idade > 18:
    print('Você Ja Deveria ter se ALISTADO')
else:
    print('ERRO Tente Novamente')

