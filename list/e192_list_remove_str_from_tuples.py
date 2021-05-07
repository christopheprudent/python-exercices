def remove_str(t):
    _t = ()
    for x in t:
        if not isinstance(x, str):
            _t = _t + (x,)

    return _t

L = [(100, 'Math'), (80, 'Math'), (90, 'Math'), (88, 'Science', 89), (90, 'Science', 92)]
print('liste', L)
print('sans les chaînes')
print(list(map(remove_str, L)))

# web solution
def test(list1):
    result =   [tuple(v for v in i if not isinstance(v, str)) for i in list1]
    return list(result)

print(test(L))
