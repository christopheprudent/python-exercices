L = (1, 2, 3, 4, 5, 6, 7, 8, 9)

_even = _odd = 0
for n in L:
    if not n % 2:
        _even += 1
    else:
        _odd += 1

print('liste', L)
print('nombre d\'éléments pairs: ', _even)
print('nombre d\'éléments impairs: ', _odd)
