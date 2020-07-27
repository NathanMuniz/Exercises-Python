salario = float(input('Qual o salario do funsionario R$'))
s = salario * 10 / 100
v = salario * 15 / 100
if salario > 1250.00:
    salari = salario + s
else:
    salari = salario + v
print('quem ganhava R${:.2f} vai recever R${:.2f} '.format(salario, salari))




