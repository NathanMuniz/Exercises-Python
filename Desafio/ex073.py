times = ('Corinthias', 'Palmeiras', 'Santos', 'Gremio',
         'Cruzeiro', 'Flamengo', 'Vasco', 'Chapecoence',
         'Atletico', 'Botafogo', 'Atleico-PR', 'Bahia',
         'São Paulo', 'Fluminense', 'Sport Recife',
         'EC Vitoria', 'Coritiva', 'Avaí', 'Ponte Preta',
         'Atletico-GO')
print('-='*15)
print(times)
print('-='*15)
print(f'Os 5 primeiros times são {times[0:5]}')
print('-='*15)
print(f'Os 4 útimos são: {times[16:20]}')
print(f'Times em ordem Alfabetica: {sorted(times)}')
print(f'O Chapecoence está na {times.index("Chapecoence")+ 1}° posição')
