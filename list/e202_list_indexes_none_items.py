def indexes_item(l, item):
    return [i for i,x in enumerate(l) if x == item]

# web solution
def relative_order(lst, item):
    result = [i for i in range(len(lst)) if lst[i] == item]
    return result

L = [1, None, 5, 1, None, 0, None, None]
print('liste', L)
print('indice des éléments égaux à None')
print(indexes_item(L, None))
print(relative_order(L, None))
print('indice des éléments égaux à 1')
print(indexes_item(L, 1))
print(relative_order(L, 1))
