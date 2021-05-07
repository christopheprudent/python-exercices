# FIXME
# out of range, if list not even!
def join_adjacent_items(l):
    return [x+L[(2*i)+1] for i,x in enumerate(L[::2])]

# web solution
def test(lst):
    result = [x + y for x, y in zip(lst[::2],lst[1::2])]
    return result
import itertools
def test2(lst):
    result = [x + y for x, y in itertools.zip_longest(lst[::2],lst[1::2], fillvalue=' ')]
    return result

L = ['1', '2', '3', '4', '5', '6', '7', '8']
print('liste', L)
print('avec concaténation des éléments consécutifs')
print(join_adjacent_items(L))
print(test(L))

L = ['1', '2', '3']
print('liste', L)
print('avec concaténation des éléments consécutifs')
#print(join_adjacent_items(L))
print(test(L))
print(test2(L))
