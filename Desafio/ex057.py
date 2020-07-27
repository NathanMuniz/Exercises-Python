
s = str(input('Digite seu  sexo [F/M]')).upper().strip()[0]
while s != 'M' and s != 'F':
    s = str(input('\033[32m Dados invaliods \033[m , Por favor  Digite  seu sexo [M][F]')).upper()
print(s)