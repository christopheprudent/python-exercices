# web solution
def func(nums, k):
    import collections
    d = collections.defaultdict(int)
    for row in nums:
        for i in row:
            d[i] += 1
    temp = []
    import heapq
    for key, v in d.items():
        if len(temp) < k:
            temp.append((v, key))
            if len(temp) == k:
                heapq.heapify(temp)
        else:
            if v > temp[0][0]:
                #heapq.heappop(temp)
                #heapq.heappush(temp, (v, key))
                heapq.heapreplace(temp, (v, key))
    result = []
    temp2 = temp.copy()
    while temp:
        v, key = heapq.heappop(temp)
        result.append(key)
    return result, temp2

import pprint
nums = [
    [1, 2, 6],
    [1, 3, 4, 5, 7, 8],
    [1, 3, 5, 6, 8, 9],
    [2, 5, 7, 11],
    [1, 4, 7, 8, 12]
]  
k = 3
print('liste')
pprint.pprint(nums)

print('Top {} des éléments les plus fréquents'.format(k))
ltop, htop = func(nums, k)
print('liste', ltop)
print('heap', htop)
