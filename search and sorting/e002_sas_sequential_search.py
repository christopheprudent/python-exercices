def sequential_search(items, item):
    _found = False
    _index = -1

    for k, v in enumerate(items):
        if v == item:
            _found = True
            _index = k

        if _found:
            break

    return (_found, _index)

# web solution
def Sequential_Search(dlist, item):
    pos = 0
    found = False
    
    while pos < len(dlist) and not found:
        if dlist[pos] == item:
            found = True
        else:
            pos = pos + 1
    
    return found, pos

def print_result(item, found, index):
    print(f'élément: {item} trouvé: {found}', end='')
    if found:
        print(f' à l\'index: {index}')
    else:
        print()

L = [11,23,58,31,56,77,43,12,65,19]
print('liste', L)
print('recherche séquentielle d\'élément')

item = 31
found, index = sequential_search(L, item)
print_result(item, found, index)
found, index = Sequential_Search(L, item)
print_result(item, found, index)

item = 19
found, index = sequential_search(L, item)
print_result(item, found, index)
found, index = Sequential_Search(L, item)
print_result(item, found, index)

item = 20
found, index = sequential_search(L, item)
print_result(item, found, index)
found, index = Sequential_Search(L, item)
print_result(item, found, index)
