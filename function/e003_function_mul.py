def f_mul(*args):
    _mul = args[0]
    for n in args[1:]:
        _mul *= n

    return _mul

print('fonction permettant de multiplier plusieurs nombres')
nums = [1, -1, 3]
print('nombres', nums, 'mul=', f_mul(*nums))
nums = [1, -1, 3, 2, 10, -5]
print('nombres', nums, 'mul=', f_mul(*nums))
