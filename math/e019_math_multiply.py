def multiply(m, n):
    _result = 0
    for _ in range(n):
        _result += m
    return _result

# web solution
def multiply_2(x, y):
    if y < 0:
        return -multiply_2(x, -y)
    elif y == 0:
        return 0
    elif y == 1:
        return x
    else:
        return x + multiply_2(x, y - 1)

if __name__ == '__main__':
    print('dev) multiplication 3x4 égale à', multiply(3, 4))
    print('web) multiplication 3x4 égale à', multiply_2(3, 4))
    print('dev) multiplication 2x6 égale à', multiply(2, 6))
    print('web) multiplication 2x6 égale à', multiply_2(2, 6))
    print('dev) multiplication 7x5 égale à', multiply(7, 5))
    print('web) multiplication 7x5 égale à', multiply_2(7, 5))
