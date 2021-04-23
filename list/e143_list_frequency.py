import collections

L=[[1, 2, 3, 2], [4, 5, 6, 2], [7, 8, 9, 5]]
c=collections.Counter([x[i] for x in L for i in range(len(x))])
print('liste', L)
print('fréquence des éléments', c)

# web solution
def count_elements_lists(nums):
    nums = [item for sublist in nums for item in sublist]
    dic_data = {}
    for num in nums:
        if num in dic_data.keys():
            dic_data[num] += 1
        else:
            dic_data[num] = 1
    return dic_data

print(count_elements_lists(L))
