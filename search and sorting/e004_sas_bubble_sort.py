# https://www.w3resource.com/python-exercises/data-structures-and-algorithms/python-search-and-sorting-exercise-4.php
def bubble_sort(items):
    todo = True
    _pass = 0
    while todo:
        _pass += 1
        todo = False
        for i in range(len(items) -1):
            if items[i] > items[i+1]:
                items[i], items[i+1] = items[i+1], items[i]
                todo = True

    print('passage: ', _pass)
    return items

# web solution
def bubbleSort(nlist):
    _pass = 0
    for passnum in range(len(nlist)-1,0,-1):
        _pass += 1
        for i in range(passnum):
            if nlist[i]>nlist[i+1]:
                temp = nlist[i]
                nlist[i] = nlist[i+1]
                nlist[i+1] = temp
    print('passage: ', _pass)

L = [14,46,43,27,57,41,45,21,70]
print('liste', L)
print('après tri')
print(bubble_sort(L))
bubbleSort(L)
print(L)
