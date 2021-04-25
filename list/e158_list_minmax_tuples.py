def minmax_tuples(l):
    _l = sorted(l, key=lambda x: x[1])
    _min = _l[0][1]
    _max = _l[-1][1]

    return _max, _min

L = [('V', 60), ('VI', 70), ('VII', 75), ('VIII', 72), ('IX', 78), ('X', 70)]
print('liste de tuples', L)
print('(max, min) =', minmax_tuples(L))

# web solution
from operator import itemgetter

def max_min_list_tuples(class_students):
    return_max = max(class_students,key=itemgetter(1))[1] 
    return_min = min(class_students,key=itemgetter(1))[1] 
    return return_max, return_min

print('(max, min) =', max_min_list_tuples(L))
