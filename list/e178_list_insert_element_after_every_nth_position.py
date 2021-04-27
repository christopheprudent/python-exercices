# web solution
def inset_element_list(lst, x, n):
    i = n
    while i < len(lst):
        lst.insert(i, x)
        i+= n+1
    return lst

L = [1, 3, 5, 7, 9, 11, 0, 2, 4, 6, 8, 10, 8, 9, 0, 4, 3, 0]
print('liste', L)
print('après insertion de {} tous les {} : {}'.format(20, 4, inset_element_list(L, 20, 4)))

L = ['s','d','f','j','s','a','j','d','f','d']
print('liste', L)
print('après insertion de {} tous les {} : {}'.format('Z', 3, inset_element_list(L, 'Z', 3)))
