def extract_list_of_lists(ld):
    return [list(d.values()) for d in ld]

# web solution
def test(dic, keys):
    return [list(d[k] for k in keys) for d in dic]

D = [
      {'student_id': 1, 'name': 'Jean Castro', 'class': 'V'}
    , {'student_id': 2, 'name': 'Lula Powell', 'class': 'V'}
    , {'student_id': 3, 'name': 'Brian Howell', 'class': 'VI'}
    , {'student_id': 4, 'name': 'Lynne Foster', 'class': 'VI'}
    , {'student_id': 5, 'name': 'Zachary Simon', 'class': 'VII'}
]
print('dictionnaire', D)
print('liste de listes des valeurs des dictionnaires')
print(extract_list_of_lists(D))

print('avec toutes les clés')
print(test(D, ('student_id', 'name', 'class')))
print('avec les clés: student_id, name')
print(test(D, ('student_id', 'name')))
print('avec les clés: name, class')
print(test(D, ('name', 'class')))
