L=['Red color', 'Orange#', 'Green', 'Orange @', 'White']
lw=['#', 'color', '@']

# web solution
def remove_words(in_list, char_list):
    new_list = []
    for line in in_list:
        new_words = ' '.join([word for word in line.split() if not any([phrase in word for phrase in char_list])])
        new_list.append(new_words)
    return new_list

print('liste', L)
print('mots séparés:', [ s for l in list(map(str.split, L)) for s in l ])
print('à exclure les mots contenant un élément de', lw, ':'
    , [ s for l in list(map(str.split, L)) for s in l if not any([w in s for w in ['#', 'color', '@']]) ]
    , 'ou'
    , remove_words(L, lw)
)
