def find_item(t, item):
    return [i for i,x in enumerate(t) if x == item]

T = 1, 2, 'a', 1, 3, 'A', 0, 'A', -1, 'A'
print('tuple', T)
print('index élément {}'.format('a'))
print(find_item(T, 'a'))
print('index élément {}'.format(1))
print(find_item(T, 1))
print('index élément {}'.format('B'))
print(find_item(T, 'B')) 

# web solution
