def interleave_elements_of_list_of_lists(ll):
    _nol = len(ll)
    _max = max(len(x) for x in ll)
    result = []
    for i in range(_max):
        for j in range(_nol):
            if i < len(ll[j]):
                result.append(ll[j][i])

    return result

LL = [
    [2, 4, 7, 0, 5, 8]
    , [2, 5, 8]
    , [0, 1]
    , [3, 3, -1, 7]
]

print('liste de listes', LL)
print('entrelacement des éléments de chaque sous-liste', interleave_elements_of_list_of_lists(LL)) 
