import collections
c = collections.Counter({"p":4, "q":2})
print('collection', c)
print('chaque élément répété selon son nombre')
print([ x for k, v in c.items() for x in k*v ])

# web solution
print(list(c.elements()))
