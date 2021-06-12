def sort_sep_words(s, sep='-'):
    _words = sorted(s.split(sep))
    return sep.join(_words)
    
S = 'green-red-yellow-black-white'
print('chaîne', S)
print('chaîne triée: ', sort_sep_words(S))

# web solution (w/ inputs)
print('entrez des couleurs, séparées par le caractère %c' % '-')
items=[n for n in input().split('-')]
items.sort()
print('-'.join(items))
