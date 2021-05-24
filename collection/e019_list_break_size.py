# FIXME
# à quoi ça sert?

# web solution
import collections as clt
def check_break_list(nums, n):
    coll_data = clt.Counter(nums)
    print(coll_data)
    for x in sorted(coll_data.keys()):
        print('clé ', x)
        for index in range(1, n):
            print('bloc ', index)
            print('élément ', x+index)
            coll_data[x+index] = coll_data[x+index]  - coll_data[x]
            print(coll_data)
            if coll_data[x+index] < 0:
                return False
    return True

nums = [1,2,3,4,5,6,7,8]
print('liste', nums)

n = 4
print('division en bloc de ', n)
print(check_break_list(nums, n))

n = 3
print('division en bloc de ', n)
print(check_break_list(nums, n))

