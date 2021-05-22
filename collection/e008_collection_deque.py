import collections

t = (2, 4, 6)
print('tuple', t)
d = collections.deque(t)
print('collection', d)

print('ajout à droite à partir d\'un itérable')
d.extend((8, 10, 12))
print(d)
print('ajout à gauche')
d.appendleft(2)
print(d)
print(type(d))
