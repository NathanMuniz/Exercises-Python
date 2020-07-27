lista = (str(input("Digite uma plavras")), str(input("Digite otra palavras")))
for palavra in lista:
    print(f"\n Na palavra {palavra.upper()} temos ", end=" ")
    for letra in palavra.upper():
        if letra in "AEIOU":
            print(letra.lower(), end=" ")
