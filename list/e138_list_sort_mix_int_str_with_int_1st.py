L = [19, 'red', 12, 'green', 'blue', 10, 'white', 'green', 1]
print('liste', L)
print('liste triée (entier en premier)', [int(x) if x.isdigit() else x for x in sorted(map(str, L))])

# web solution
def sort_mixed_list(mixed_list):
    int_part = sorted([i for i in mixed_list if type(i) is int])
    str_part = sorted([i for i in mixed_list if type(i) is str])
    return int_part + str_part

print('liste triée (entier en premier)', sort_mixed_list(L))
