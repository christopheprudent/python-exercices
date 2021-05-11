# web soution
num_list = [1, 2, 3, 4]
new_dict = current = {}
print(id(new_dict))
print(id(current))
for name in num_list:
    print('ajout clé {} au dictionnaire courant'.format(name))
    current[name] = {}
    print(id(current))
    print(current.keys())

    print('changement du dictionnaire courant avec le nouveau ajouté en tant que dictionnaire vide')
    current = current[name]
    print(id(current))

    # current = {}
    print(new_dict)

print('liste convertie en dictionnaires imbriqués')
print(new_dict)
