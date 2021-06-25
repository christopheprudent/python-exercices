convert_int = lambda x : tuple(map(int, filter(lambda s : s.isdigit(), x)))

TT = (('233', 'ABCD', '33'), ('1416', 'EFGH', '55'), ('2345', 'WERT', '34'))
print('tuple de tuples', TT)
print('conversion en entier')
print('mine:', tuple(map(convert_int, TT)))
