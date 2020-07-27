from time import sleep
#Variaveis
resposta = 0

#Primeira atibuição de valores
n1 = int(input('Digite o primeiro valor:'))
n2 = int(input('Digite o segundo valor :'))
soma = n1 + n2
multiplicar = n1 * n2

#Enquanto não sair do programa
while resposta != 5:
        resposta  = int(input('''
[ 1 ] somar
[ 2 ] multiplicar
[ 3 ] maior
[ 4 ] novos números
[ 5 ] sair do programa
Escolha Uma das opições:'''))

#Se fOR SOMA
        if resposta == 1:
            print('A soma de {} + {} = {}'.format(n1, n2, soma))
#Se for multiplacaçao
        elif resposta == 2 :
            print('A multiplicaçõa de {} * {} = {}'.format(n1, n2, multiplicar))
#Se for Maior
        elif resposta == 3:
            if n1 < n2:
                print('O maior é o {}'.format(n2))
            else:
                print('O maior é o {}'.format(n1))
#se for Novos Numeros
        elif resposta == 4:
            n1 = int(input('Digite o primeiro valor:'))
            n2 = int(input('Digite o segundo valor :'))
            soma = n1 + n2
            multiplicar = n1 * n2
#Dgitação errada
        elif resposta != 1 or 2 or 3 or 4 :
            print('Resposata invalida, Tente novamente')
#Algo a mais
        sleep(1.25)
print('FIM')



