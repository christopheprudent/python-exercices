def remove_item_from_list(ld, item):
    # web solution: x.get('id') != item
    return [x for x in ld if x['id'] != item]

LD = [{'id': '#FF0000', 'color': 'Red'}, {'id': '#800000', 'color': 'Maroon'}, {'id': '#FFFF00', 'color': 'Yellow'}, {'id': '#808000', 'color': 'Olive'}]
print('liste de dictionnaires', LD)
print('sans celui contenant id égal à {}'.format('#808000'))
print(remove_item_from_list(LD, '#808000'))
