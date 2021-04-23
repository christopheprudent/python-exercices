def sort_str_as_int(l):
    return sorted(map(int, l))

L = ['4', '12', '45', '7', '0', '100', '200', '-12', '-500']
print('liste', L)
print('tri numérique', sort_str_as_int(L))
