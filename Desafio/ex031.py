destancia = float(input('Qual é a distancia da viagem?'))
preço1 = destancia*0.50
presço2 = destancia*0.45
if destancia <= 200:
    print('Você esta preste a começar uma viagem de {:.0f}.0Km.'.format(destancia))
    print('E o Preço de Sua parasagem sera de R${:.2f}'.format(preço1))
else:
    print('Você esta peste a começar uma viagem de {:.0f}.0K'.format(destancia))
    print('E o preço de sua pasagem sera de R${:.2f}'.format(presço2))


