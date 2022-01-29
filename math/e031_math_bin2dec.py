def bin2dec(b):
    """
    >>> bin='11001'
    >>> [ int(c) for c in bin ]
    [1, 1, 0, 0, 1]
    >>> l1=[ int(c) for c in bin ]
    >>> l2=l1[::-1]
    >>> l2
    [1, 0, 0, 1, 1]
    >>> d = [v * 10 ** i for i, v in enumerate(l2)]
    >>> d
    [1, 0, 0, 1000, 10000]
    >>> d = [v * 2 ** i for i, v in enumerate(l2)]
    >>> d
    [1, 0, 0, 8, 16]
    >>> sum(d)
    25
    """

    _t1 = [int(c) for c in b]
    _t2 = _t1[::-1]
    _d1 = [v * 2 ** i for i, v in enumerate(_t2)]
    return sum(_d1)

# web solution
def binary_to_decimal(b):
    value = 0
    b_num = list(b)
    for i in range(len(b_num)):
        digit = b_num.pop()
        if digit == '1':
            value = value + pow(2, i)

    return value

if __name__ == '__main__':
    n = input('Entrer un nombre binaire : ')
    print('dev) nombre converti en décimal', bin2dec(n))
    print('web) nombre converti en décimal', binary_to_decimal(n))
