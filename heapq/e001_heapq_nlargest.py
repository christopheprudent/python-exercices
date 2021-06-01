import heapq

nums_list = [25, 35, 22, 85, 14, 65, 75, 22, 58]
heapq.heapify(nums_list)
print('heapq', nums_list)
n = 3
print('les {} plus grands éléments sont {}'.format(n, heapq.nlargest(n, nums_list)))
