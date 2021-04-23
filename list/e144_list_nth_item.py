def nth_item(l, nth):
    return [x[i] for x in L for i in range(len(x)) if i==nth]

L=[[1, 2, 3, 2], [4, 5, 6, 2], [7, 1, 9, 5]]
print('liste', L)
print('chaque {}e élément: {}'.format(1, nth_item(L, 0)))
print('chaque {}e élément: {}'.format(3, nth_item(L, 2)))

# web solution
def specified_element(nums, N):
    result = [i[N] for i in nums]
    return result

print('chaque {}e élément: {}'.format(1, specified_element(L, 0)))
print('chaque {}e élément: {}'.format(3, specified_element(L, 2)))
