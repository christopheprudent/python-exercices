D = {'x':500, 'y':5874, 'z': 560}
print('dictionnaire', D)
print('valeur minimale', min(D.values()))
print('valeur maximale', max(D.values()))

# web solution
key_max = max(D.keys(), key=(lambda k: D[k]))
key_min = min(D.keys(), key=(lambda k: D[k]))

print('Maximum: ',D[key_max])
print('Minimum: ',D[key_min])
