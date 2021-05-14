D = {'C1': [10, 20, 30], 'C2': [20, 30, 40], 'C3': [12, 34]}
print('dictionnaire', D)
print('après effacement des listes')
#print({(k,[]) for k in D.keys()})
D2 = dict()
for k in D.keys():
    D2[k] = []
print(D2)

# web solution
def test(dictionary):
    for key in dictionary:
        dictionary[key].clear()
    return dictionary

print(test(D))
