peso = float(input(' Qunato Você pesa?(KG)'))
altura = float(input('Qual sua altura (M)'))
imc = peso / (altura ** 2)
print('O Imc Da pessoa è de {:.1f}'.format(imc))
if imc < 18.5:
    print('Abaixo do Peso')
elif imc < 25:
    print('Pesso Ideal')
elif imc < 30:
    print('SOBREPESO')
elif imc < 40:
    print('OBESIDADE')
else:
    print('OBESIDADE MORBIA')

