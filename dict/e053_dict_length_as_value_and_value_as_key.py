def length_as_value_and_value_as_key(d):
    return dict((v,len(v)) for v in d.values())
    

D = {1: 'red', 2: 'green', 3: 'black', 4: 'white', 5: 'black'}
# waited: {'red': 3, 'green': 5, 'black': 5, 'white': 5}
print('dictionnaire', D)
print('après transformation: dictionnaire des valeurs avec leur longueur associée')
print(length_as_value_and_value_as_key(D))

D = {'1': 'Austin Little', '2': 'Natasha Howard', '3': 'Alfred Mullins', '4': 'Jamie Rowe'}
print('dictionnaire', D)
print('après transformation: dictionnaire des valeurs avec leur longueur associée')
print(length_as_value_and_value_as_key(D))
