def list_remove_nth_column(l, c):
    c -= 1
    if 0 <= c <= len(l):
        return [ x for i, x in enumerate(l) if i != c ]

    return l

# web solution
def remove_column(nums, n):
    for i in nums: 
        del i[n]
    return nums

L = [[1, 2, 3], [2, 4, 5], [1, 1, 1]]
print('liste', L)
print('sans la colonne 1:', [list_remove_nth_column(l, 1) for l in L])
print('sans la colonne 1:', remove_column(L, 0))

L = [[1, 2, 3], [-2, 4, -5], [1, -1, 1]]
print('liste', L)
print('sans la colonne 3:', [list_remove_nth_column(l, 3) for l in L])
print('sans la colonne 3:', remove_column(L, 2))
