s = str(input('Informe seu sexo: [M,F]')).upper()
while s not in 'MmFf':
    s = str(input('Dados inválidos.Por favor, informe seu sexo: [M,F] '))
