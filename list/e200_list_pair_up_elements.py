def pair_up_elements(l):
    return [[x,y] for x,y in zip(l, l[1:])]

# web solution
def pair_consecutive_elements(lst):
    result = [[lst[i], lst[i+1]] for i in range(len(lst) - 1)]
    return result

L = [1, 2, 3, 4, 5, 6]
print('liste', L)
print('avec regroupement des éléments de rang (i, i+1)')
print(pair_up_elements(L))
print(pair_consecutive_elements(L))
