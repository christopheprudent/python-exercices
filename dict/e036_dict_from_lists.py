import collections

def create_dict_from_lists(l1, l2, sol = 'mine'):
    d = collections.defaultdict(set)
    for k,v in zip(l1, l2):
        if sol == 'mine':
            d[k] = d[k].union({v})
        else:
            d[k].add(v)

    return d

L1 = ['Class-V', 'Class-VI', 'Class-VII', 'Class-VIII', 'Class-V']
L2 = [1, 2, 2, 3, 4]
print('liste1', L1)
print('liste2', L2)
print('création dictionnaire à partir de ces 2 listes')
print(create_dict_from_lists(L1, L2))
# web solution
print(create_dict_from_lists(L1, L2, 'web'))
