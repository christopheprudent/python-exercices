import collections

L = ['Green', 'Red', 'Blue', 'Red', 'Orange', 'Black', 'Black', 'White', 'Orange']
print('liste', L)
print('occurences des éléments')
print(collections.Counter(L))

L = [3, 5, 0, 3, 9, 5, 8, 0, 3, 8, 5, 8, 3, 5, 8, 1, 0, 2]
print('liste', L)
print('occurences des éléments')
print(collections.Counter(L))
