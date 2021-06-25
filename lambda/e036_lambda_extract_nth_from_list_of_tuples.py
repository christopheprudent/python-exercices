extract_nth = lambda l, n : [ x[n] for x in l ]

# web solution
def extract_nth_element(test_list, n):
    result = list(map (lambda x:(x[n]), test_list))
    return result

LT = [('Greyson Fulton', 98, 99), ('Brady Kent', 97, 96), ('Wyatt Knott', 91, 94), ('Beau Turnbull', 94, 98)]
print('liste de tuples', LT)
for i in range(1, len(LT[0])+1):
    print('seulement la liste des éléments de rang', i, ': mine', extract_nth(LT, i-1), 'web', extract_nth_element(LT, i-1))
