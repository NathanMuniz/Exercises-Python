from datetime import date
idad = int(input('Que ano Vêce nasceu?'))
idade = date.today().year - idad
print('O Atleta Que tem {}'.format(idade))
if idade <= 9:
    print('Classificão :MIRIM')
elif idade > 9 and idade <= 14:
    print('Classificaçãoa :INFANTIL')
elif idade > 14 and idade <= 19:
    print('Classificação :JUNIOR')
elif idade > 19 and idade <= 25 :
    print('Classificação : SêNIOR')
elif idade > 25:
    print('Classificação : MASTER')



