tote18 = homem = mulheres = 0
while True:
    print('-' * 20)
    print('Cadastre uma pessoa')
    print('-' * 20)
    idade = int(input('Idade:'))
    soxo = ''
    while soxo != 'FM':
        sexo = str(input('Sexo [F/M]:')).strip().upper()[0]
    if idade >= 18:
        tote18 += 1
    if sexo == 'M':
        homem += 1
    if sexo == 'F' and idade < 20:
        mulheres += 1
    conti = ' '
    while conti != 'SN':
        conti = str(input('Quer Continuar ? [S/N]')).upper().strip()[0]
    if conti == 'N':
        break

print(f'''Total de passoas com mais de 18 anos:{tote18}
      Ao Todo temos  {homem} cadastrado
      E temos  {mulheres} mulheres com menos de Vinte ''')