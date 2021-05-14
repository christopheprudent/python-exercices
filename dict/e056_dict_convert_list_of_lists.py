# web solution
def test(d):
    result = list(map(list, d.items()))
    return result 

D = {1: 'red', 2: 'green', 3: 'black', 4: 'white', 5: 'black'}
print('dictionnaire', D)
print('conversion en liste de listes')
print([[x,y] for (x,y) in D.items()])
print(test(D))

D = {'1': 'Austin Little', '2': 'Natasha Howard', '3': 'Alfred Mullins', '4': 'Jamie Rowe'}
print('dictionnaire', D)
print('conversion en liste de listes')
print([[x,y] for (x,y) in D.items()])
print(test(D))
