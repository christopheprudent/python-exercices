import collections

S = 'Python Exercises Practice Solution Exercises'
L = S.split()
C = collections.Counter(L)

print('chaîne de mots', S)
print('sans les duplications')
print(' '.join(C.keys()))

# web solution
print(' '.join(collections.OrderedDict((w,w) for w in S.split()).keys()))
