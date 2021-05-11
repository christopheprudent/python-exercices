# https://stackoverflow.com/questions/3939361/remove-specific-characters-from-a-string-in-python

def remove_space_from_keys(d):
    nd = dict()
    for k, v in d.items():
        if ' ' in k:
            k = k.translate({ord(c): None for c in ' '})

        nd[k] = v

    return nd

D = {'S  001': ['Math', 'Science'], 'S    002': ['Math', 'English']}
print('dictionnaire', D)
print('clés sans espace')
print(remove_space_from_keys(D))

# web solution
ND = {x.translate({32: None}): y for x, y in D.items()}
print(ND)
