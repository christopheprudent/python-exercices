def index_minmax(l):
    _len = len(l)
    _min = min(l)
    _max = max(l)

    imin = [ i for i in range(_len) if l[i] == _min ]
    imax = [ i for i in range(_len) if l[i] == _max ]

    return imin, imax

L = [12, 33, 23, 10, 67, 89, 45, 667, 23, 12, 11, 10, 54]
print('liste', L)
print('positions des valeurs (min, max):', index_minmax(L))
