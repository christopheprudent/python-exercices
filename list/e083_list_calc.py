def sum_mult_by_len(ln):
    t = map(round, ln)
    s = sum(t)
    c = s * len(ln)
    return c

L = [22.4, 4.0, -16.22, -9.1, 11.0, -12.22, 14.2, -5.2, 17.5]
print('liste ', L)
print('calcul somme(éléments arrondis) * nb éléments : ', sum_mult_by_len(L))
