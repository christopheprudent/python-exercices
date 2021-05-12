def drop_empty_from_dict(d):
    nd = dict()
    for k,v in d.items():
        if v:
            nd[k] = v

    return nd

# web solution
def drop_if_None(d):
    return {key:value for (key, value) in d.items() if value is not None}

D = {'c1': 'Red', 'c2': 'Green', 'c3': None}
print('dictionnaire', D)
print('sans les éléments vides')
print(drop_empty_from_dict(D))
print(drop_if_None(D))
