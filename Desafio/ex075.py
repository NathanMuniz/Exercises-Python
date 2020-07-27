num = (int(input("Digite um número")), int(input("Digite outro número")),
       int(input("Digite uma um número")), int(input("Digite o útimo número")))
print(f"Você digitou os valores {num}")
print(f"O valor 9 apareceu {num.count(9)} Veses")
if 3 in num:
    print(f"O valor 3 apareceu na {num.index(3) + 1}° Posiçãio")
else:
    print('O valor 3 não apareceu na Trupla')
print("O valores pares foram: ", end=' ')
for n in num:
    if n % 2 == 0:
        print(n, end=" ")


