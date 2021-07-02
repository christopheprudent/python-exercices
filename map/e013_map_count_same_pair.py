# web solution
from operator import eq
def count_same_pair(nums1, nums2):
    result = sum(map(eq, nums1, nums2))
    return result

nums1 = [1,2,3,4,5,6,7,8]
nums2 = [2,2,3,1,2,6,7,9]
print('liste 1', nums1)
print('liste 2', nums2)
print('nombre de pairs égales')
print(count_same_pair(nums1, nums2))
