# bad idea!
def get_1st_greater_than(l, x):
    _sorted = sorted(l)
    print(f'_sorted={_sorted}')
    try:
        _i = _sorted.index(x) +1
        while _i <= len(l):
            print(f'_i={_i} {_sorted[_i]}')
            if _sorted[_i] > x:
                return l.index(_sorted[_i])

            _i += 1
        return None

    except ValueError:
        return None


def get_1st_greater_than(l, x):
    for i, v in enumerate(l):
        if v > x:
            return i

L = [12, 45, 23, 67, 78, 90, 100, 76, 38, 62, 73, 29, 83]
print('liste', L)
print('index du plus grand élément que {} est {}'.format(73, get_1st_greater_than(L, 73)))
print('index du plus grand élément que {} est {}'.format(21, get_1st_greater_than(L, 21)))
print('index du plus grand élément que {} est {}'.format(80, get_1st_greater_than(L, 80)))
print('index du plus grand élément que {} est {}'.format(55, get_1st_greater_than(L, 55)))

# web solution
def first_index(l, n):
    return next(a[0] for a in enumerate(l) if a[1] > n)

print('index du plus grand élément que {} est {}'.format(73, first_index(L, 73)))
print('index du plus grand élément que {} est {}'.format(21, first_index(L, 21)))
print('index du plus grand élément que {} est {}'.format(80, first_index(L, 80)))
print('index du plus grand élément que {} est {}'.format(55, first_index(L, 55)))
