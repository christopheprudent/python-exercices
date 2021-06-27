sort_mixed = lambda l : sorted(filter(lambda x : isinstance(x, int), l)) + sorted(filter(lambda x : isinstance(x, str), l))

# web solution
def sort_mixed_list(mixed_list):
    mixed_list.sort(key=lambda e: (isinstance(e, str), e))
    return mixed_list

L = [19, 'red', 12, 'green', 'blue', 10, 'white', 'green', 1]
print('liste', L)
print('liste triée, avec les entiers en premier')
print('mine:', sort_mixed(L))
print(' web:', sort_mixed_list(L))
