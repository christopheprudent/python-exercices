def concat_items_of_tuple(t):
    _concat=''
    for item in t:
        if _concat:
            _concat+=' '
        _concat+=item
    return _concat

# web solution
def tuples_to_list_string(lst):
    result = list(map(' '.join, lst))
    return result

colors = [('red', 'pink'), ('white', 'black'), ('orange', 'green')]
print('liste de tuples')
print(colors)
print('convertie en liste de chaînes')
print('mine:', list(map(concat_items_of_tuple, colors)))
print(' web:', tuples_to_list_string(colors))
