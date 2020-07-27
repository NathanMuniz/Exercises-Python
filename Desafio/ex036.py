
casa = float(input('Valor da casa:R$'))
salario = float(input('Salario so comprador: R$'))
anos = int(input('Em caquantos anos'))
prestasão = casa / (anos*12)
minimo = salario * 30 / 100
print('Para pagar um casa de R${}  em {} anos,'.format(casa, anos), end='')
print('prestação sera de R${:.2f} '.format(prestasão))
if prestasão <= minimo:
    print('Emprestimo CONCEDIDO')
else:
    print('Emprestimo NEGADO')


