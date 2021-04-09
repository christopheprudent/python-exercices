L = [1, 2, 3, 4]
prefix = 'emp'
print("Original List: ", L)
L2 = [prefix + str(elt) for elt in L]
print("resulting List: ", L2)

# web solution
print(['emp{0}'.format(i) for i in  L])
