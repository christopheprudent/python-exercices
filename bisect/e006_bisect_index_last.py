import bisect

def index(a, x):
    """
    trouve la dernière occurence de x dans a (trié)
    """
    i = bisect.bisect_right(a, x)
    if i > 0 and a[i-1] == x:
        return i-1
    raise ValueError

L = [1, 2, 3, 4, 8, 8, 10, 12]
print('liste', L)
n = 8
print('dernière occurence de {} : {}'.format(n, index(L, n)))
n = 12
print('dernière occurence de {} : {}'.format(n, index(L, n)))
n = 1
print('dernière occurence de {} : {}'.format(n, index(L, n)))
