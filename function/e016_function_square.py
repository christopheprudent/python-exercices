def square_numbers(n):
    _squares = []
    for i in range(1, n+1):
        _squares.append(i*i)

    return _squares

n = 30
print('liste des carrés de 1 à %d' % n)
print(square_numbers(n))
