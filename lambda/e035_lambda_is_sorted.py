is_sorted = lambda l : all(x <= y for x, y in zip(l, l[1:]))

# web solution
def is_sort_list(nums, key=lambda x: x):
    for i, e in enumerate(nums[1:]):
        if key(e) < key(nums[i]): 
            return False
    return True

def is_sort_list2(nums):
    for i, e in enumerate(nums[1:]):
        if e < nums[i]: 
            return False
    return True

L = [1, 2, 4, 6, 8, 10, 12, 14, 16, 17]
print('liste', L)
print('cette est-elle triée? ', 'mine:', is_sorted(L), 'web:', is_sort_list(L), 'web-mine:', is_sort_list2(L))

L = [2,3,8,4,7,9,8,2,6,5,1,6,1,2,3,4,6,9,1,2]
print('liste', L)
print('cette est-elle triée? ', 'mine:', is_sorted(L), 'web:', is_sort_list(L), 'web-mine:', is_sort_list2(L))
