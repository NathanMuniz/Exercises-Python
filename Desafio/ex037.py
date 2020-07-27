num = int(input('Digite um numero inteiro'))
print('''Escolha uma das bases para conversão:
[1] Converter para Binario
[2] Converter para Octal
[3] Converter para Hexadecimal''')
opsão = int(input('Sua Opção:'))
if opsão == 1:
    print('Se {} For convertido em BINARIO é igual a {}'.format(num, bin(num)[2:]))
elif opsão == 2:
    print('Se {} Convertido em Octal é igual a {}'.format(num, oct(num)[2:]))
elif opsão == 3:
    print('Se {} For Convertido em HEXADECIMAL è igual a {}'.format(num, hex(num)[2:]))
else:
    print('Opção invalida tente novamente')
