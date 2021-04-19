import itertools

# web solution
def unique_sublists(input_list):
    result ={}
    for l in input_list: 
        result.setdefault(tuple(l), list()).append(1) 
    print('result (setdefault):', result)
    for a, b in result.items(): 
        result[a] = sum(b)
    return result

L = [[1, 3], [5, 7], [1, 3], [13, 15, 17], [5, 7], [9, 11]]
print('liste', L)
print('sous-listes:', [ (key, len(list(group))) for key, group in itertools.groupby(sorted(L)) ])
print('sous-listes:', unique_sublists(L))

L = [['green', 'orange'], ['black'], ['green', 'orange'], ['white']]
print('liste', L)
print('sous-listes:', [ (key, len(list(group))) for key, group in itertools.groupby(sorted(L)) ])
print('sous-listes:', unique_sublists(L))
