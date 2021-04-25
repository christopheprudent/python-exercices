def words_as_list_of_chars(l):
    return [list(x) for x in l]

L = ['Red', 'Maroon', 'Yellow', 'Olive']
print('liste', L)
print('chaque mot décomposé en liste de caractères', words_as_list_of_chars(L))
