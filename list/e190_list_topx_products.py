import itertools

def topx_products(l1, l2, x):
    #p = list(itertools.product(L1, L2))
    return sorted([i*j for i, j in itertools.product(L1, L2)])[-x:]

# web solution
def top_product(nums1, nums2, N):
    result = sorted([x*y for x in nums1 for y in nums2], reverse=True)[:N]
    return result

L1 = [1, 2, 3, 4, 5, 6]
L2 = [3, 6, 8, 9, 10, 6]
print('listes')
print(L1)
print(L2)

print('top {} des produits de ces 2 listes:\n{}'.format(3, topx_products(L1, L2, 3)))
print(top_product(L1, L2, 3))
print('top {} des produits de ces 2 listes:\n{}'.format(4, topx_products(L1, L2, 4)))
print(top_product(L1, L2, 4))
