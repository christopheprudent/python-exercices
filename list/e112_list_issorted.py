def issorted(l):
    return all(y > x for x, y in zip(l, l[1:]))

# web solution
def is_sort_list(nums):
    result = all(nums[i] <= nums[i+1] for i in range(len(nums)-1))
    return result

L = [1, 2, 4, 6, 8, 10, 12, 14, 16, 17]
print('Liste', L)
print('est triée:', issorted(L))
print('est triée:', is_sort_list(L))

L = [2,3,8,4,7,9,8,2,6,5,1,6,1,2,3,4,6,9,1,2]
print('Liste', L)
print('est triée:', issorted(L))
print('est triée:', is_sort_list(L))
