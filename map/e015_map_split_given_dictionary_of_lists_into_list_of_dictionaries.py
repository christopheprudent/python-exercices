# web solution
def list_of_dicts(marks):
    result = map(dict, zip(*[[(key, val) for val in value] for key, value in marks.items()]))
    return list(result)

# [(key, value) for key, value in marks.items()]
# [('Science', [88, 89, 62, 95]), ('Language', [77, 78, 84, 80])]
# [[(key, val) for val in value] for key, value in marks.items()]
# [[('Science', 88), ('Science', 89), ('Science', 62), ('Science', 95)], [('Language', 77), ('Language', 78), ('Language', 84), ('Language', 80)]]
# list(zip(*[[(key, val) for val in value] for key, value in marks.items()]))
# [(('Science', 88), ('Language', 77)), (('Science', 89), ('Language', 78)), (('Science', 62), ('Language', 84)), (('Science', 95), ('Language', 80))]
# list(map(dict, zip(*[[(key, val) for val in value] for key, value in marks.items()])))
# [{'Science': 88, 'Language': 77}, {'Science': 89, 'Language': 78}, {'Science': 62, 'Language': 84}, {'Science': 95, 'Language': 80}]

marks = {'Science': [88, 89, 62, 95], 'Language': [77, 78, 84, 80]}
print('dictionnaire de listes')
print(marks)
print('converti en liste de dictionnaires')
print(list_of_dicts(marks))
