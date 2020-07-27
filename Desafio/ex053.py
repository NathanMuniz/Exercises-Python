frase =str(input('Digite Uma Frase')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''
for letra in range(len(junto) -1, -1, -1):
    inverso += junto[letra]
if inverso == junto:
    print('Isso é um Palídromo')
else:
    print('A frase Digitada não é um palidromo')

