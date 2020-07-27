print('►'*20)
print('Seja Bem Vindo Ao Bnaco ceV')
print('►'*20)
valor = int(input('Qula valor você quer sacar ? R$'))
cinco = vinte = dez = um = 0
while valor >= 50:
    valor -= 50
    cinco += 1
if cinco >= 1:
    print(f'Total de {cinco} cèdulas de R$:50')
while valor >= 20:
    valor -= 20
    vinte += 1
if vinte >= 1:
    print(f'Total de {vinte} células de R$20')
while valor >= 10:
    valor -= 10
    dez += 1
if dez >= 1:
    print(f'Total de {dez} cédulas de R$10')
while valor >= 1:
    valor -= 1
    um += 1
if um >= 1:
    print(f'Total de {um} cédulas de R$1')
print('►'*20)
print('Volte sempre ao banco cev! Tenha um bom dia ')