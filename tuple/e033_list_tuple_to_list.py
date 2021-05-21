def convert_list_of_tuples_to_list_of_lists(l):
    return list(map(list, l))

print('conversion liste de tuples en liste de listes')
L=[(1, 2), (2, 3), (3, 4)]
print('liste', L)
print(convert_list_of_tuples_to_list_of_lists(L))

L=[(1, 2, 6), (2, 3, -6), (3, 4), (2, 2, 2, 2)]
print('liste', L)
print(convert_list_of_tuples_to_list_of_lists(L))
