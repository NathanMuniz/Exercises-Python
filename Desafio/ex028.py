import random
num1 = int(input('Adivinhe o numero que estou pensando de 0 a 5:'))
num = random.randint(0, 5)
if num == num1:
    print('Parabéns vovê acertou era mesmo o numero {} '.format(num))
else:
    print('Que pena você erou era o {} tente novamente'.format(num))




