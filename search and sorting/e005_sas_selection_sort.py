# https://www.w3resource.com/python-exercises/data-structures-and-algorithms/python-search-and-sorting-exercise-5.php
# pour chaque élément, échanger (si possible) avec le plus petit trouvé parmi les élémentys suivants
def selection_sort(items):
    for i in range(len(items)):
        k = i
        for j in range(i+1, len(items)):
            if items[k] > items[j]:
                k = j
        if k != i:
            items[i], items[k] = items[k], items[i]

    return items

# web solution
def selectionSort(nlist):
   for fillslot in range(len(nlist)-1,0,-1):
       maxpos=0
       for location in range(1,fillslot+1):
           if nlist[location]>nlist[maxpos]:
               maxpos = location

       # optimisation
       if maxpos != fillslot:
           print(f'échange({nlist[fillslot]}, {nlist[maxpos]})') 
           temp = nlist[fillslot]
           nlist[fillslot] = nlist[maxpos]
           nlist[maxpos] = temp
           print(f'i={fillslot} max={maxpos} {nlist}') 

L = [14,46,43,27,57,41,45,21,70]
print('liste', L)
print('après tri')
print(selection_sort(L))
L = [14,46,43,27,57,41,45,21,70]
print('liste', L)
print('après tri')
selectionSort(L)
print(L)
