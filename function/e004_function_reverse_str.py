def str_reverse(s):
    _str = ''
    for i in range(len(s)-1, -1, -1):
        _str += s[i]

    return _str

S = "1234abcd"
print('chaîne:', S, 'inversée:', str_reverse(S))
