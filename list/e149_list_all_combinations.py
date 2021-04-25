# https://stackoverflow.com/questions/464864/how-to-get-all-possible-combinations-of-a-list-s-elements
from itertools import chain, combinations
def all_subsets(ss):
    return chain(*map(lambda x: combinations(ss, x), range(0, len(ss)+1)))

L = ['orange', 'red', 'green', 'blue']
print('liste', L)
print('combinaisons:')
for subset in all_subsets(L):
    print(subset)

# web solution
def combinations_list(colors):
    if len(colors) == 0:
        return [[]]
    result = []
    for el in combinations_list(colors[1:]):
        result += [el, el+[colors[0]]]
    return result

print('\ntoutes les combinaisons', combinations_list(L))
