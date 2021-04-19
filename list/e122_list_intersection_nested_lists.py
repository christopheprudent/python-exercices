def intersection_nested_lists(ll):
    inter = ll[0]
    for i in range(1, len(ll)):
        inter = list(set(inter).intersection(ll[i]))

    return inter

# web solution
def common_in_nested_lists(nested_list):
    result = list(set.intersection(*map(set, nested_list)))
    return result

L = [[12, 18, 23, 25, 45], [7, 12, 18, 24, 28], [1, 5, 8, 12, 15, 16, 18]]
print('liste de listes', L)
print('éléménts communes entre chaque sous-liste', intersection_nested_lists(L), common_in_nested_lists(L))
