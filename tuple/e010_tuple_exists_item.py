def exists_item(t, item):
    return item in t

T = 1, 2, 'a', 1, 3, 'A', 0, 'A', -1, 'A'
print('tuple', T)
print('existence élément {}'.format('a'))
print(exists_item(T, 'a'))
print('existence élément {}'.format(-1))
print(exists_item(T, -1))
print('existence élément {}'.format('B'))
print(exists_item(T, 'B')) 
