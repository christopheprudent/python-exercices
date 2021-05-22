# https://stackoverflow.com/questions/9819602/union-of-dict-objects-in-python
import itertools

def union_dicts(*dicts):
    return dict(itertools.chain.from_iterable(dct.items() for dct in dicts))

# web solution
import collections

def merge_dictionaries(*dicts):
    merged_dict = dict(collections.ChainMap({}, *dicts))
    return merged_dict

D1 = {'R': 'Red', 'B': 'Black', 'P': 'Pink'}
D2 = {'G': 'Green', 'W': 'White'}
D3 = {'O': 'Orange', 'W': 'White', 'B': 'Black'}

print('Dict 1', D1)
print('Dict 2', D2)
print('Dict 3', D3)

print()
print('D1|D2', union_dicts(D1, D2))
print('D1|D2', merge_dictionaries(D1, D2))
print('D1|D2|D3', union_dicts(D1, D2, D3))
print('D1|D2|D3', merge_dictionaries(D1, D2, D3))
