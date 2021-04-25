import itertools

def add_elements_of_lists(l1, l2):
    return [x+y for x, y in itertools.zip_longest(l1, l2, fillvalue=0)]

L1 = [2, 4, 7, 0, 5, 8]
L2 = [3, 3, -1, 7]
print('liste 1:', L1)
print('liste 2:', L2)
print('somme des éléments correspondants (par la gauche)', add_elements_of_lists(L1, L2))

# web solution
def elementswise_left_join(l1, l2):
    f_len = len(l1)-(len(l2) - 1)
    for i in range(0, len(l2), 1):
        if f_len - i >= len(l1):
            break
        else:
            l1[i] = l1[i] + l2[i]
    return l1

print('somme des éléments correspondants', elementswise_left_join(L1, L2))
