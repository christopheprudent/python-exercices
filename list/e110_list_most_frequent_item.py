import collections
def most_frequent_item(l):
    c = collections.Counter(l)
    return c.most_common(1)

L = [2, 3, 8, 4, 7, 9, 8, 2, 6, 5, 1, 6, 1, 2, 3, 4, 6, 9, 1, 2]
print('Liste', L)
mc = most_frequent_item(L)[0]
print('élément le plus fréquent est {} avec {} occurrence(s)'.format(mc[0], mc[1])) 
