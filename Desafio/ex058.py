import random
print('''Sou seu computador ...
Acabei de pensar em um numero de 0 a 10 
Será que você consegue adivinhar qual foi?''')
c = random.randint(0, 10)
s = 0
p = int(input('Qual é seu palpite?'))
while p != c:
    p = int(input('Você\033[31m Eroou\033[m,Tente Novamente! '))
    s = s + 1
print('Você \033[34mAcertou\033[m Com \033[33m{} Tentativas '.format(s))
