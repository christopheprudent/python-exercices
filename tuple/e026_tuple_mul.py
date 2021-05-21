import operator, functools

T=(4, 3, 2, 2, -1, 18)
print('tuple', T)
print('produit des membres')
print(functools.reduce(operator.mul, T, 1))

T=(2, 4, 8, 8, 3, 2, 9)
print('tuple', T)
print('produit des membres')
print(functools.reduce(operator.mul, T, 1))

# web solution
def mutiple_tuple(nums):
    product = 1 
    for x in nums:
        product *= x
    return product

print(mutiple_tuple(T))
