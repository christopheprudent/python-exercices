def move_item_at_end(l, item):
    l.append(l.pop(l.index(item)))
    return l

L = ['red', 'green', 'white', 'black', 'orange']
print('liste', L)
print('déplacer (white) à la fin')
print(move_item_at_end(L, 'white'))

L = ['red', 'green', 'white', 'black', 'orange']
print('liste', L)
print('déplacer (red) à la fin')
print(move_item_at_end(L, 'red'))

L = ['red', 'green', 'white', 'black', 'orange']
print('liste', L)
print('déplacer (black) à la fin')
print(move_item_at_end(L, 'black'))
