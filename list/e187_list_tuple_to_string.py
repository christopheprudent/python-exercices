def tuples_to_string(t):
    tmp = ''
    for e in t:
        tmp += e + ' '
    return tmp[:-1]

# web solution
def tuples_to_list_str(lst):
    # https://docs.python.org/fr/3/tutorial/inputoutput.html
    # §7.1.4 'string' % values (interpolation de chaîne de caractères)
    # el -> (red, green) #2, soit '%s %s ' % (red, green)
    # strip pour supprimer l'espace terminal!
    result = [("%s "*len(el)%el).strip() for el in lst]
    return result

L = [('red', 'green'), ('black', 'white'), ('orange', 'pink')]
print('liste', L)
print('conversion tuples en chaînes')
print(list(map(tuples_to_string, L)))
print(tuples_to_list_str(L))

L = [('Laiba', 'Delacruz'), ('Mali', 'Stacey', 'Drummond'), ('Raja', 'Welch'), ('Saarah', 'Stone')]
print('liste', L)
print('conversion tuples en chaînes')
print(list(map(tuples_to_string, L)))
print(tuples_to_list_str(L))
