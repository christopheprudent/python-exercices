def replace_last_value(lt, value):
    return [t[:-1] + (value,) for t in lt]

L = [(10, 20, 40), (40, 50, 60), (70, 80, 90)]
print('liste', L)
print('changement dernière valeur avec {0}'.format(100)) 
print(replace_last_value(L, 100))
