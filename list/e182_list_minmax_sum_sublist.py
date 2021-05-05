def minmax_sum_sublist(ll):
    _lsum = [(i, sum(x)) for i, x in enumerate(ll)]
    _lsum_sort=sorted(_lsum, key=lambda x: x[1])

    return _lsum_sort[0][0], _lsum_sort[-1][0]

# web solution
def max_min_sublist(lst):
    max_result = max(lst, key=sum)
    min_result = min(lst, key=sum)
    return max_result,min_result

L=[[1, 2, 3, 5], [2, 3, 5, 4], [0, 5, 4, 1], [3, 7, 2, 1], [1, 2, 1, 2]]
print('liste', L)
m, M = minmax_sum_sublist(L)
print('élements de somme min, de somme max sont {} et {}, soit les sous-listes {} et {}'.format(m, M, L[m], L[M]))

result = max_min_sublist(L)
print('élément de somme max', result[0])
print('élément de somme min', result[1])
