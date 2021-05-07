import itertools

def sum_list_by_position(ll):
    #return [x+y+z for x,y,z in itertools.zip_longest(ll[0], ll[1], ll[2], fillvalue=0)]
    return [sum(x) for x in itertools.zip_longest(*ll, fillvalue=0)]

# web solution
def sum_lists_diff_length(test_list):
    result =  [sum(x) for x in zip(*map(lambda x:x+[0]*max(map(len, test_list)) if len(x)<max(map(len, test_list)) else x, test_list))]
    return result


L = [[1, 2, 4], [2, 4, 4], [1, 2]]
print('liste', L)
print('sommes par position respective')
print(sum_list_by_position(L))
print(sum_lists_diff_length(L))

L = [[1], [2, 4, 4], [1, 2], [4]]
print('liste', L)
print('sommes par position respective')
print(sum_list_by_position(L))
print(sum_lists_diff_length(L))
