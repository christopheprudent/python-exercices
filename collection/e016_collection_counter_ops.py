import collections

C1 = collections.Counter({1: 1, 2: 1, 3: 1, 4: 1, 5: 1})
C2 = collections.Counter({4: 1, 5: 1, 6: 1, 7: 1, 8: 1})
print('Counter 1', C1)
print('Counter 2', C2)
print()
print('C1+C2', C1+C2)
print('C1-C2', C1-C2)
print('C2-C1', C2-C1)
print('C1&C2', C1&C2)
print('C1|C2', C1|C2)
