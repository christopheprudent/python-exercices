import collections, itertools

def get_occurs(ll):
    c = collections.Counter(itertools.chain.from_iterable(ll))
    return c

L = [[1, 2, 3, 2], [4, 5, 6, 2], [7, 1, 9, 5]]
print('liste', L)
print('fréquence des éléments')
print(get_occurs(L))
