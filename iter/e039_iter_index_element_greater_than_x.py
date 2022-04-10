# web solution
from itertools import takewhile

def first_index(l1, n):
    #return len(list(takewhile(lambda x: x[1] <= n, enumerate(l1))))
    return len(list(takewhile(lambda x: x <= n, l1)))


nums = [12,45,23,67,78,90,100,76,38,62,73,29,83]
print("Original list:")
print(nums)
n = 73
ix = first_index(nums,n)
print("\nIndex of the first element which is greater than",n,"in the said list:", ix, ":", nums[ix])
n = 21
ix = first_index(nums,n)
print("\nIndex of the first element which is greater than",n,"in the said list:", ix, ":", nums[ix])
n = 80
ix = first_index(nums,n)
print("\nIndex of the first element which is greater than",n,"in the said list:", ix, ":", nums[ix])
n = 55
ix = first_index(nums,n)
print("\nIndex of the first element which is greater than",n,"in the said list:", ix, ":", nums[ix])
