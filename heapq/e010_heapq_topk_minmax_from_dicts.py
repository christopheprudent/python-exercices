# web solution
import heapq
from pprint import pprint
items = [
    {'name': 'Item-1', 'price': 101.1},
    {'name': 'Item-2', 'price': 555.22},
    {'name': 'Item-3', 'price': 45.09},
    {'name': 'Item-4', 'price': 22.75},
    {'name': 'Item-5', 'price': 16.30},
    {'name': 'Item-6', 'price': 110.65}
]

cheap = heapq.nsmallest(3, items, key=lambda s: s['price'])
expensive = heapq.nlargest(3, items, key=lambda s: s['price'])
print('ensemble des éléments (avec leur prix)')
pprint(items)
print('\nTop 3 des éléments les plus chers')
pprint(expensive)
print('\nTop 3 des éléments les moins chers')
pprint(cheap)
