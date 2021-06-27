# web solution
def count_occurrences(nums):

    # list(map(lambda el : (el, nums.count(el)), nums))
    # [(3, 4), (4, 2), (5, 3), (8, 2), (0, 2), (3, 4), (8, 2), (5, 3), (0, 2), (3, 4), (1, 1), (5, 3), (2, 2), (3, 4), (4, 2), (2, 2)]
    # dict permet d'unifier les couples (x, occur(x))

    result = dict(map(lambda el : (el, nums.count(el)), nums))
    return result

nums = [3, 4, 5, 8, 0, 3, 8, 5, 0, 3, 1, 5, 2, 3, 4, 2]
print('liste', nums)
print('comptage des occurrences des éléments')
print(' web:', count_occurrences(nums))
