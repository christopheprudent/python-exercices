# web solution

import itertools

print('somme de chaque chiffre de chaque nombre d\'une liste')
nums = [10,2,56]
print('liste', nums)
print('web', sum(int(c) for c in itertools.chain(*[str(x) for x in nums])))
print('dev', sum(int(c) for x in map(str, nums) if x.isdigit() for c in x))

nums = [123,25,56]
print('liste', nums)
print('web', sum(int(c) for c in itertools.chain(*[str(x) for x in nums])))
print('dev', sum(int(c) for x in map(str, nums) if x.isdigit() for c in x))
