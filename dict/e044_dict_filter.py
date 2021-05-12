D = {'Cierra Vega': (6.2, 70), 'Alden Cantrell': (5.9, 65), 'Kierra Gentry': (6.0, 68), 'Pierre Cox': (5.8, 66)}
print('dictionnaire', D)
print('seulement les éléments de hauteur > 6 et poids >= 70')
D2 = filter(lambda x:x[1][0]>6 and x[1][1]>=70, D.items())
print({k:v for k,v in D2})

# web solution
D3 = {key:value for (key, value) in D.items() if value[0] > 6 and value[1]>=70}
print(D3)
