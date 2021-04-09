def insert_before_each_item(l, b):
    for i, v in enumerate(b):
        l.insert(i*2, v)

    return l

L = [1, 2, 3, 4]
B = ['a', 'b', 'c', 'd', 'e', 'f']
print(insert_before_each_item(L, B))

# web solution
color = ['Red', 'Green', 'Black']
print("Original List: ",color)
# append constant ('c') before each ones
color = [v for elt in color for v in ('c', elt)]
print("resulting List: ",color)
