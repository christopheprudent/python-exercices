def list_move_value_at_end(l, v):
    lv = [ v for x in l if x == v ]
    lnv = [ x for x in l if x != v ]
    return lnv + lv

L = [3, 4, 0, 0, 0, 6, 2, 0, 6, 7, 6, 0, 0, 0, 9, 10, 7, 4, 4, 5, 3, 0, 0, 2, 9, 7, 1]
print('Liste: ', L)
print('result: ', list_move_value_at_end(L, 0))

# web solution
print('at begin: ', sorted(L, key= lambda x: x != 0))
print('at end: ', sorted(L, key= lambda x: x == 0))
