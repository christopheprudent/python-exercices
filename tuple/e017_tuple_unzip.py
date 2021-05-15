# web solution
l = [(1,2), (3,4), (8,9)]
print('liste de tuples', l)
print('unzip')
t1, t2 = list(zip(*l))
print('tuple 1', t1)
print('tuple 2', t2)
print('zip')
l2 = list(zip(t1, t2))
print('liste de tuples', l2)
