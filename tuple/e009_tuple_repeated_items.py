import collections

def repeated_items(t):
    c = collections.Counter(t)
    return [k for k,v in c.items() if v > 1]

T = 1, 2, 'a', 1, 3, 'A', 0, 'A', -1, 'A'
print('tuple', T)
print('éléments multiples')
print(repeated_items(T)) 
