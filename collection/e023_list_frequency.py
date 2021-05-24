import collections

L=[(['1', '4'], ['4', '1'], ['3', '4'], ['2', '7'], ['6', '8'], ['5', '8'], ['6', '8'], ['5', '7'], ['2', '7'])]
print('liste', L)
print('transformation en liste de tuples')
L2=[(x[0], x[1]) if x[0] <= x[1] else (x[1], x[0]) for x in L[0]]
#[('1', '4'), ('1', '4'), ('3', '4'), ('2', '7'), ('6', '8'), ('5', '8'), ('6', '8'), ('5', '7'), ('2', '7')]
print(L2)
c = collections.Counter(L2)
#Counter({('1', '4'): 2, ('2', '7'): 2, ('6', '8'): 2, ('3', '4'): 1, ('5', '8'): 1, ('5', '7'): 1})
print(c)

# web solution (sort)
result = collections.Counter(tuple(sorted(i)) for i in L[0])
print("\nTuples","     ","occurence")
for key,val in result.items():
    print(key," ", val)
