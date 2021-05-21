def tuple_ints_to_int(t):
    return int(''.join(map(str, t)))

T = (1, 2, 3)
print('tuple', T)
print('conversion en 1 nombre entier (par concaténation des nombres)')
print(tuple_ints_to_int(T))

T = (10, 20, 40, 5, 70)
print('tuple', T)
print('conversion en 1 nombre entier (par concaténation des nombres)')
print(tuple_ints_to_int(T))
