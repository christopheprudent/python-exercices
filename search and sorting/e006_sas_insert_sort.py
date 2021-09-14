# https://www.w3resource.com/python-exercises/data-structures-and-algorithms/python-search-and-sorting-exercise-6.php
def insert_sort(items):
    todo = True
    while todo:
        todo = False
        for i in range(0, len(items) -1):
            j = i
            for j in range(i+1, 0, -1):
                if items[j-1] > items[j]:
                    todo = True
                    items[j-1], items[j] = items[j], items[j-1]
                else:
                    break
                
# web solution
def insertionSort(nlist):
    for index in range(1,len(nlist)):

        currentvalue = nlist[index]
        position = index

        while position>0 and nlist[position-1]>currentvalue:
            nlist[position]=nlist[position-1]
            position = position-1

        # optimisation
        if position != index:
            nlist[position]=currentvalue
            print(f'current={currentvalue} index={index} position={position} {nlist}')


L = [14,46,43,27,57,41,45,21,70]
print('liste', L)
print('après tri insertion')
insert_sort(L)
print(L)

L = [14,46,43,27,57,41,45,21,70]
print('liste', L)
print('après tri insertion')
insertionSort(L)
print(L)
