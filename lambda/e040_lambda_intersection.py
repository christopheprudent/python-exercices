L = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
LL = [[12, 18, 23, 25, 45], [7, 11, 19, 24, 28], [1, 5, 8, 18, 15, 16]]

# web solution
def intersection_nested_lists(l1, l2):
    result = [list(filter(lambda x: x in l1, sublist)) for sublist in l2]
    return result

inter_list = lambda l, ll : [list(set(x) & set(l)) for x in ll]

print('liste de listes', LL)
print('autre liste', L)
print('intersection des listes avec autre liste')
print('mine:', inter_list(L, LL))
print(' web:', intersection_nested_lists(L, LL))
