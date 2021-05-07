def indexes_of_common_items(l1, l2):
    return [i for i,x in enumerate(l1) if x in L2]

L1 = [1, 2, 3, 4, 5, 6]
L2 = [7, 8, 5, 2, 10, 12]
print('liste1', L1)
print('liste2', L2)
print('indice des éléments communs')
print(indexes_of_common_items(L1, L2))

L2 = [7, 8, 5, 7, 10, 12]
print('liste1', L1)
print('liste2', L2)
print('indice des éléments communs')
print(indexes_of_common_items(L1, L2))

L1 = [1, 2, 3, 4, 15, 6]
print('liste1', L1)
print('liste2', L2)
print('indice des éléments communs')
print(indexes_of_common_items(L1, L2))
