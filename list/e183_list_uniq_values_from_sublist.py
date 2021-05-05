def uniq_values_from_sublist(ll):
    uniqs = []
    for l in ll:
        for e in l:
            if e not in uniqs:
                uniqs.append(e)

    return uniqs

# web solution
def unique_values_in_list_of_lists(lst):
    result = set(x for l in lst for x in l)
    return list(result)

L = [[1, 2, 3, 5], [2, 3, 5, 4], [0, 5, 4, 1], [3, 7, 2, 1], [1, 2, 1, 2]]
print('liste', L)
print('seulement les éléments uniques')
print(uniq_values_from_sublist(L))
print(unique_values_in_list_of_lists(L))

L = [['h', 'g', 'l', 'k'], ['a', 'b', 'd', 'e', 'c'], ['j', 'i', 'y'], ['n', 'b', 'v', 'c'], ['x', 'z']]
print('liste', L)
print('seulement les éléments uniques')
print(uniq_values_from_sublist(L))
print(unique_values_in_list_of_lists(L))
