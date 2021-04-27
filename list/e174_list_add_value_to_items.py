def add_value_to_items(l, val):
    return [x+val for x in l]

L = [3, 8, 9, 4, 5, 0, 5, 0, 3]
print('liste', L)
print('ajout valeur {} à tous les éléments: {}'.format(3, add_value_to_items(L, 3)))
L = [3.2, 8, 9.9, 4.2, 5, 0.1, 5, 3.11, 0]
print('liste', L)
print('ajout valeur {} à tous les éléments: {}'.format(0.51, add_value_to_items(L, 0.51)))
