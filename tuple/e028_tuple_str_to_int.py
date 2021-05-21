def convert_tuple_str_to_int(t):
    return tuple(tuple(map(int, list(x))) for x in t)

T = (('333', '33'), ('1416', '55'))
print('tuple', T)
print('conversion en nombre entier')
print(convert_tuple_str_to_int(T))
