def get_1st_even_odd(l):
    _even = min(l, key= lambda x: x%2)
    _odd = min(l, key= lambda x: not x%2)
    return _even, _odd

# web:
def first_even(lst):
    return next((e for e in lst if not e%2), -1)
def first_odd(lst):
    return next((e for e in lst if e%2), -1)

L = [1, 3, 5, 7, 4, 1, 6, 8]
print('liste', L)
print('premiers éléments pair & impair:', get_1st_even_odd(L))
print('premier élément pair:', first_even(L))
print('premier élément impair:', first_odd(L))
