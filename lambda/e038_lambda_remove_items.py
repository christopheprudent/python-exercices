remove_items = lambda l1, l2 : [x for x in l1 if x not in l2]

# web solution
def remove_items_list(list1, list2):
    result = list(filter(lambda x: x not in list2, list1))
    return result

list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list2 = [2, 4, 6, 8]
print('liste 1', list1)
print('liste 2', list2)
print('seulement les éléments de liste 1 non présents dans liste 2')
print('mine:', remove_items(list1, list2))
print(' web:', remove_items_list(list1, list2))
