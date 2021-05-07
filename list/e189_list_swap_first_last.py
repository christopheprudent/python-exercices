def swap_first_last(l):
    l[0], l[-1] = l[-1], l[0]
    return l

# web solution
def shift_first_last(lst):
    x = lst.pop(0)
    y = lst.pop()
    lst.insert(0, y)
    lst.insert(len(lst), x)
    return lst

L = [1, 2, 3, 4, 5, 6, 7]
print('liste', L)
print('après échange premier/dernier')
print(swap_first_last(L))
print(shift_first_last(L))

L = ['s', 'd', 'f', 'd', 's', 's', 'd', 'f']
print('liste', L)
print('après échange premier/dernier')
print(swap_first_last(L))
print(shift_first_last(L))
