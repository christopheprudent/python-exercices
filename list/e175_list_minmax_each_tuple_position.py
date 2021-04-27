def minmax_each_tuple_position(lt):
    _max0 = max(lt, key=lambda x: x[0])[0]
    _max1 = max(lt, key=lambda x: x[1])[1]
    _min0 = min(lt, key=lambda x: x[0])[0]
    _min1 = min(lt, key=lambda x: x[1])[1]

    return [_max0, _max1], [_min0, _min1]

L = [(2, 3), (2, 4), (0, 6), (7, 1)]
print('liste', L)
print('max(position 0, position 1) min(position 0, position 1)', minmax_each_tuple_position(L))

# web solution
def max_min_list_tuples(nums):
    result1 = map(max, zip(*nums))
    result2 = map(min, zip(*nums))
    return list(result1), list(result2)

print('max(position 0, position 1) min(position 0, position 1)', max_min_list_tuples(L))
