def count_sublist_contains_element(ll, e):
    return sum(1 for l in ll if e in l)

L = [[1, 3], [5, 7], [1, 11], [1, 15, 7]]
print('liste', L)
print('nombre de sous-liste(s) contenant', 3, count_sublist_contains_element(L, 3))
print('nombre de sous-liste(s) contenant', 2, count_sublist_contains_element(L, 2))
print('nombre de sous-liste(s) contenant', 7, count_sublist_contains_element(L, 7))

L = [['A', 'B'], ['A', 'C'], ['A', 'D', 'E'], ['B', 'C', 'D']]
print('liste', L)
print('nombre de sous-liste(s) contenant', 'A', count_sublist_contains_element(L, 'A'))
print('nombre de sous-liste(s) contenant', 'E', count_sublist_contains_element(L, 'E'))
