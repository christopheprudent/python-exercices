avg_tuple_of_tuples = lambda tt : tuple(sum(x)/len(x) for x in zip(*tt))

# web solution
def average_tuple(nums):
    result = tuple(map(lambda x: sum(x) / float(len(x)), zip(*nums)))
    return result

TT = ((10, 10, 10), (30, 45, 56), (81, 80, 39), (1, 2, 3))
print('tuple de tuples', TT)
print('moyenne des éléments de même rang de chaque sous-tuple')
print('mine:', avg_tuple_of_tuples(TT))
print(' web:', average_tuple(TT))
