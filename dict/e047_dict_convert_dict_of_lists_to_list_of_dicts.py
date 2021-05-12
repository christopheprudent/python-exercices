# FIXME
# ne marche que pour l'exemple, avec 2 clés! voir la solution ci-dessous
def convert_dict_of_lists_to_list_of_dicts(dl):
    K = list(dl.keys())
    return [{K[0]:x, K[1]:y} for x,y in zip(dl[K[0]], dl[K[1]])]

# web solution (OK pour n clés!)
def list_of_dicts(marks):
    keys = marks.keys()
    vals = zip(*[marks[k] for k in keys])
    #print(list(vals))
    #[(88, 77), (89, 78), (62, 84), (95, 80)]
    result = [dict(zip(keys, v)) for v in vals]
    return result

#D = {'Science': [88, 89, 62, 95], 'Language': [77, 78, 84, 80]}
# à transformer en: [{'Science': 88, 'Language': 77}, {'Science': 89, 'Language': 78}, {'Science': 62, 'Language': 84}, {'Science': 95, 'Language': 80}]
D = {'Science': [88, 89, 62, 95], 'Language': [77, 78, 84, 80], 'History': [10, 20, 30, 40]}
print('dictionnaire', D)
print('après transformation du dictionnaire de listes en liste de dictionnaires')
print(convert_dict_of_lists_to_list_of_dicts(D))
print(list_of_dicts(D))
