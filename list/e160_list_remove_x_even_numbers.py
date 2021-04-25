def remove_x_even_numbers(l, x):
    _result = []
    _n = 0
    for i in range(len(l)):
        if _n < x and not l[i] % 2:
            _n += 1
            continue

        _result.append(l[i])

    return _result

L = [3,10,4,7,5,7,8,3,3,4,5,9,3,4,9,8,5]
n = 4
print('liste', L)
print('après suppression des {} premiers nombres pairs: {}'.format(n, remove_x_even_numbers(L, n)))

# web solution
def condition_match(x):
    return ((x % 2) == 0)
def remove_items_con(data, N):
    ctr = 1
    result = []
    for x in data:
        if ctr > N or not condition_match(x):
            result.append(x)
        else:
            ctr = ctr + 1
    return result

print('après suppression des {} premiers nombres pairs: {}'.format(n, remove_items_con(L, n)))
