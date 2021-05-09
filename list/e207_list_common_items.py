def common_items(l1, l2):
    return [x for x in l1 if x in l2]

# web solution
def test(list1, list2):
    result =  set(list1).intersection(list2)
    return list(result)

L1 = [('red', 'green'), ('black', 'white'), ('orange', 'pink')]
L2 = [('red', 'green'), ('orange', 'pink')]
print('liste1', L1)
print('liste2', L2)
print('éléments communs (liste1,liste2)')
print(common_items(L1, L2))
print(test(L1, L2))

print('éléments communs (liste2,liste1)')
print(common_items(L2, L1))
print(test(L2, L1))
