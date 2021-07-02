# web solution
nums1 = [1, 2, 3] 
nums2 = [4, 5, 6] 
nums3 = [7, 8, 9] 
print('listes')
print(nums1)  
print(nums2)  
print(nums3)  
result = map(lambda x, y, z: x + y + z, nums1, nums2, nums3) 
print('somme des éléments des 3 listes')
print('mine:', [x+y+z for x, y, z in zip(nums1, nums2, nums3)])
print(' web:', list(result))
