def dict_from_string(s):
    d = dict()
    for c in s:
        d[c] = d.get(c, 0) +1

    return d

S = 'w3resource'
print('chaîne', S)
print('transformée en dictionnaire, en comptant les occurences de ses lettres')
print(dict_from_string(S))
