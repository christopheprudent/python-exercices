import array

#FIXME éléments consécutifs!
def first_dup(a):
    for x, y in zip(a, a[1:]):
        if x == y:
            return x
    return -1

def first_dup2(a):
    t = array.array('i', a)
    for x in t:
        if t.count(x) > 1:
            return x
    return -1

# web solution
def find_first_duplicate(nums):
    num_set = set()
    no_duplicate = -1

    for i in range(len(nums)):

        if nums[i] in num_set:
            return nums[i]
        else:
            num_set.add(nums[i])

    return no_duplicate

A = [1, 2, 3, 4, 4, 5]
print('tableau', A)
print('premier doublon: ', first_dup(A), first_dup2(A))
print(find_first_duplicate(A))

A = [1, 2, 3, 4]
print('tableau', A)
print('premier doublon: ', first_dup(A), first_dup2(A))
print(find_first_duplicate(A))

A = [1, 1, 2, 3, 3, 2, 2]
print('tableau', A)
print('premier doublon: ', first_dup(A), first_dup2(A))
print(find_first_duplicate(A))

A = [1, 4, 1, 3, 3, 2, 2]
print('tableau', A)
print('premier doublon: ', first_dup(A), first_dup2(A))
print(find_first_duplicate(A))
