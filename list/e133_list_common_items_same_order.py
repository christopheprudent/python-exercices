import itertools

def common_items_same_order(l1, l2):
    d1={v: k for k, v in enumerate(l1)}
    d2={v: k for k, v in enumerate(l2)}
    return not any(d2[x] > d2[y] for x, y in list(itertools.combinations(l1, 2)) if x in l2 and y in l2 and d1[x] < d1[y])

# web solution
def same_order(l1, l2):
    common_elements = set(l1) & set(l2)
    l1 = [e for e in l1 if e in common_elements]
    l2 = [e for e in l2 if e in common_elements]
    return l1 == l2

L1=['red', 'green', 'black', 'orange']
L2=['red', 'pink', 'green', 'white', 'black']
L3=['white', 'orange', 'pink', 'black']

print('liste1', L1)
print('liste2', L2)
print('liste3', L3)
print('même ordre entre (L1, L2)', common_items_same_order(L1, L2), same_order(L1, L2))
print('même ordre entre (L1, L3)', common_items_same_order(L1, L3), same_order(L1, L3))
print('même ordre entre (L2, L3)', common_items_same_order(L2, L3), same_order(L2, L3))
