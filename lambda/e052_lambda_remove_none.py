remove_none = lambda l : [x for x in l if x != None]

# web solution
def remove_none2(nums):
    result = filter(lambda v: v is not None, nums)
    return list(result)

L = [12, 0, None, 23, None, -55, 234, 89, None, 0, 6, -12]
print('liste', L)
print('sans le éléments de valeur NONE')
print('mine:', remove_none(L))
print(' web:', remove_none2(L))
