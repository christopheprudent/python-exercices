def tuple_exists_item(t, item):
    return any(item in x for x in t)

T = (('Red', 'White', 'Blue'), ('Green', 'Pink', 'Purple'), ('Orange', 'Yellow', 'Lime'))
print('tuple', T)
print('élément {} est présent: {}'.format('White', tuple_exists_item(T, 'White')))
print('élément {} est présent: {}'.format('Olive', tuple_exists_item(T, 'Olive')))
