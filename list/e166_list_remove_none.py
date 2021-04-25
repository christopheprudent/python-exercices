def remove_none(l):
    return [x for x in L if x is not None]

L = [12, 0, None, 23, None, -55, 234, 89, None, 0, 6, -12]
print('liste', L)
print('sans les éléments nuls (None)', remove_none(L))
