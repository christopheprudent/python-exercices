def merge_some_items(l, i, j):
    l[i:j] = [''.join(l[i:j])]
    return l

L = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
print('liste', L)
print('fusion des éléments de {} à {} : {}'.format(2, 4, merge_some_items(L, 2, 4)))
