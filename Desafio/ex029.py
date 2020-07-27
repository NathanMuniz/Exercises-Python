velocidade = float(input('Escreva a Velocidade de seu carro:'))
if velocidade <=80:
    print('Tenha um bom dia.Dirija com segurança')
else:
    print('MUTADO.Você passou o limite permitodo que è 80km/h')
    print('Você agora vai ter que pagar de R${:.2f}!'.format((velocidade - 80 )*7))
    print('Tenha um bom dia . Digija com segurança')
