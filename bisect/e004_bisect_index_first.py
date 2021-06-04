import bisect

def index(a, x):
    """
    trouve la première occurence de x dans a (trié)
    """
    i = bisect.bisect_left(a, x)
    if i != len(a) and a[i] == x:
        return i
    raise ValueError

L = [1, 2, 3, 4, 8, 8, 10, 12]
n = 8
print('liste', L)
print('première occurence de {} : {}'.format(n, index(L, n)))
