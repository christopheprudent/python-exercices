def remove_item(t, item):
    return tuple(x for x in t if x != item)

T = 1, 2, 'a', 1, 3, 'A', 0, 'A', -1, 'A'
print('tuple', T)
print('effacement élément {}'.format('a'))
print(remove_item(T, 'a'))
print('effacement élément {}'.format(-1))
print(remove_item(T, -1))
print('effacement élément {}'.format('B'))
print(remove_item(T, 'B')) 

# web solution
#create a tuple
tuplex = "w", 3, "r", "e", "s", "o", "u", "r", "c", "e"
print('\n')
print(tuplex)
#tuples are immutable, so you can not remove elements
#using merge of tuples with the + operator you can remove an item and it will create a new tuple
print('effacement élément {}'.format('r'))
tuplex = tuplex[:2] + tuplex[3:]
print(tuplex)
#converting the tuple to list
listx = list(tuplex) 
#use different ways to remove an item of the list
print('effacement élément {}'.format('c'))
listx.remove("c") 
#converting the tuple to list
tuplex = tuple(listx)
print(tuplex)
