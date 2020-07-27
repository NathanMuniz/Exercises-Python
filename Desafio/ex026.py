frase = str (input('Digite alguma frase')).strip()
frases = frase.upper()
print('aparece {} vezes a letra a'.format(frases.count('A')))
primeira = frases.find('A')+1
print('Aparece a primeira vez na possisâo{}'.format(primeira))
print('A utima letra a aparece na posisâo {}'.format(frases.rfind('A')+1))


