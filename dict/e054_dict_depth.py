# web solution
def dict_depth(d):
    print(f'd={d}')
    if isinstance(d, dict):
        _depth=1 + (max(map(dict_depth, d.values())) if d else 0)
        print(f'_depth={_depth}')
        return _depth

    print(f'_depth=0')
    return 0

dic = {'a':1, 'b': {'c': {'d': {}}}}
print('dictionnaire', dic)
print('profondeur du dictionnaire')
print(dict_depth(dic))
