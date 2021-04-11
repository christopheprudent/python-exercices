def ll_subset_ll(ll1, ll2):
    return all(l in ll2 for l in ll1)

# web solution
def checkSubset(input_list1, input_list2): 
    return all(map(input_list1.__contains__, input_list2)) 

L1 = [[1, 3], [5, 7], [9, 11], [13, 15, 17]]
L2 = [[1, 3], [13, 15, 17]]
print('liste l1', L1)
print('liste l2', L2)
print('l2 sous-liste de l1:', ll_subset_ll(L2, L1))
print('l2 sous-liste de l1:', checkSubset(L1, L2))

L1 = [[[1, 2], [2, 3]], [[3, 4], [5, 6]]]
L2 = [[[3, 4], [5, 6]]]
print('liste l1', L1)
print('liste l2', L2)
print('l2 sous-liste de l1:', ll_subset_ll(L2, L1))
print('l2 sous-liste de l1:', checkSubset(L1, L2))

L1 = [[[1, 2], [2, 3]], [[3, 4], [5, 7]]]
L2 = [[[3, 4], [5, 6]]]
print('liste l1', L1)
print('liste l2', L2)
print('l2 sous-liste de l1:', ll_subset_ll(L2, L1))
print('l2 sous-liste de l1:', checkSubset(L1, L2))
