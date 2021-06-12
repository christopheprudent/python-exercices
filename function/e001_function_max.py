def f_max(*args):
    _max = args[0]
    for n in args[1:]:
        if n > _max:
            _max = n

    return _max

print('fonction permettant de trouver le max entre plusieurs nombres')
nums = [1, -1, 0]
print('nombres', nums, 'max=', f_max(*nums))
nums = [1, -1, 0, 2, 10, -5]
print('nombres', nums, 'max=', f_max(*nums))
