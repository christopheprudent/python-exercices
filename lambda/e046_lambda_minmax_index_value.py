import functools

def min_index_value(l):
    min_value = functools.reduce(lambda a, b : a if a <= b else b, l, l[0])
    min_index = [i for i, v in enumerate(l) if v == min_value]
    if len(min_index) == 1:
        min_index = min_index[0]
    return (min_index, min_value)

def max_index_value(l):
    max_value = functools.reduce(lambda a, b : a if a >= b else b, l, l[0])
    max_index = [i for i, v in enumerate(l) if v == max_value]
    if len(max_index) == 1:
        max_index = max_index[0]
    return (max_index, max_value)

# web solution
def position_max_min(nums):
    max_result = max(enumerate(nums), key=lambda x: x[1])
    min_result = min(enumerate(nums), key=lambda x: x[1])
    return max_result,min_result

L = [12, 33, 23, 10.11, 67, 89, 45, 66.7, 23, 12, 11, 10.25, 54, 89]
print('liste', L)
print('minimum/maximum (position, valeur)')
print('mine:', 'min', min_index_value(L))
print('maxe:', 'max', max_index_value(L))

M, m = position_max_min(L)
print('mine:', 'min', m)
print('maxe:', 'max', M)
