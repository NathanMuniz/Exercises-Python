expr = str(input('Digite Uma Espressão'))
lista = list()
for simb in expr:
    if simb == '(':
        lista.append('(')
    elif simb == ')':
        if len(lista) > 0:
            lista.pop()
        elif len(lista) == 0:
            lista.append(')')
            break
if len(lista) == 0:
    print('Sua Expressão é Válida!')
else:
    print('Sua Expressão é Invalida!')
