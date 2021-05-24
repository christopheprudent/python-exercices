import collections

l1 = [1,1,2,3,3,4,4,5,6,7]
l2 = [1,1,2,4,5,6]
c1 = collections.Counter(l1)
c2 = collections.Counter(l2)

print('liste 1', l1)
print('liste 2', l2)
print('différence: l1-l2')
print(list((c1-c2).elements()))
