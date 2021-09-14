# web solution
def shellSort(alist):
    sublistcount = len(alist)//2
    while sublistcount > 0:
        for start_position in range(sublistcount):
            gap_InsertionSort(alist, start_position, sublistcount)

        print("après gap=", sublistcount, "liste", nlist)

        sublistcount = sublistcount // 2

def gap_InsertionSort(nlist,start,gap):
    print(f' de {start+gap} à {len(nlist)} par pas de {gap}')
    for i in range(start+gap,len(nlist),gap):

        current_value = nlist[i]
        position = i

        while position>=gap and nlist[position-gap]>current_value:
            nlist[position]=nlist[position-gap]
            position = position-gap

        nlist[position]=current_value

        print(f' gap={gap} i={i} {nlist}')


nlist = [14,46,43,27,57,41,45,21,70]
print('liste', nlist)
print('après tri shell')
shellSort(nlist)
print(nlist)
