import collections

# web solution
def max_occurrences(nums):
    dict = collections.defaultdict(int)
    for i in nums:
        dict[i] += 1
    result = max(dict.items(), key=lambda x: x[1]) 
    return result

L = [2, 3, 8, 4, 7, 9, 8, 2, 6, 5, 1, 6, 1, 2, 3, 2, 4, 6, 9, 1, 2]
print('liste', L)
c = collections.Counter(L)
item, occurs = c.most_common(1)[0]
print('élément {} a la plus grande occurence #{}'.format(item, occurs))

print('élément de plus grande occurence')
print(max_occurrences(L))
