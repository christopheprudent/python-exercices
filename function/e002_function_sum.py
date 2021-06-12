def f_sum(*args):
    _sum = args[0]
    for n in args[1:]:
        _sum += n

    return _sum

print('fonction permettant de trouver la somme de plusieurs nombres')
nums = [1, -1, 0]
print('nombres', nums, 'sum=', f_sum(*nums))
nums = [1, -1, 0, 2, 10, -5]
print('nombres', nums, 'sum=', f_sum(*nums))
