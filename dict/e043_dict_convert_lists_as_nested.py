def convert_lists_as_nested(l1, l2, l3):
    return [{x:{y:z}} for x,y,z in zip(l1, l2, l3)]

L1 = ['S001', 'S002', 'S003', 'S004']
L2 = ['Adina Park', 'Leyton Marsh', 'Duncan Boyle', 'Saim Richards']
L3 = [85, 98, 89, 92]
print(convert_lists_as_nested(L1, L2, L3))
