D = {'Cierra Vega': 175, 'Alden Cantrell': 180, 'Kierra Gentry': 165, 'Pierre Cox': 190}
print('dictionnaire', D)
print('seulement les éléments dont la valeur est plus grande que 170')
D2 = filter(lambda x:x[1]>=170, D.items())
print({k:v for k,v in D2})

# web solution
D3 = {key:value for (key, value) in D.items() if value >= 170}
print(D3)
