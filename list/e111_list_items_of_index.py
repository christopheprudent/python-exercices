L = [2, 3, 8, 4, 7, 9, 8, 2, 6, 5, 1, 6, 1, 2, 3, 4, 6, 9, 1, 2]
I = [0, 3, 5, 7, 10]

print('liste', L)
print('positions demandées', I)
print('valeurs:', [v for i, v in enumerate(L) if i in I])

# web solution
def access_elements(nums, list_index):
    result = [nums[i] for i in list_index]
    return result

print(access_elements(L, I))
