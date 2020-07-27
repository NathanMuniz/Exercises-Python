nome = str (input('Qaul é o seu nome?')).strip()
n =nome.split()
print('Prazer em te cnhecer {}'.format(nome))
print('Seu primeiro nome è {}'.format(n[0]))
print('e seu utimo nome è {}'.format(n[len(n)-1]))

