#Trupla de números por extenço, nùmeros escritos.
numero = ('zero', 'Um', 'Dois', 'Tres', 'Quatro', 'Cinco', 'Seis', 'Sete',
          'oito', 'Nove', 'Dez', 'Onze', 'Doze', 'Treze', 'Quatorze', 'Quinze',
          'Desesis', 'Desesete', 'Desoioto', 'Desenove', 'Vinte')

#Analisar se o número esta entre 0 e 20
while True:
    num = int(input('Digite um núnero de 0 a 20: '))
    if num <= 20 and num >= 0:
        print(f'O número que você digitou foi {numero[num]}')
        continuar = str(input('Você quer continuar? [S/N]')).upper()
        if continuar in "NÃO": #Se o programa vai continuar ou não
            break
    else:
        print('Erro, Tente Novamente!', end=" ")



