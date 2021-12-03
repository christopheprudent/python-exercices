# https://rosettacode.org/wiki/Sorting_algorithms/Cycle_sort#Python

def cycleSort(vector):
    """
    Sort a vector in place and return the number of writes.
    """
    writes = 0
 
    print(f'vector={vector}')
    # Loop through the vector to find cycles to rotate.
    for cycleStart, item in enumerate(vector):
        print(f'(cycleStart, item)= ({cycleStart}, {item})')
 
        # Find where to put the item.
        pos = cycleStart
        for item2 in vector[cycleStart + 1:]:
            if item2 < item:
                pos += 1
 
        print(f' pos={pos}')
        # If the item is already there, this is not a cycle.
        if pos == cycleStart:
            continue
 
        # Otherwise, put the item there or right after any duplicates.
        while item == vector[pos]:
            pos += 1
        print(f'pos={pos} : swap([{pos}]={vector[pos]},item={item})')
        vector[pos], item = item, vector[pos]
        writes += 1
        print(f'writes={writes} : {vector}, item={item}')
 
        # Rotate the rest of the cycle.
        while pos != cycleStart:
 
            # Find where to put the item.
            pos = cycleStart
            for item2 in vector[cycleStart + 1:]:
                if item2 < item:
                    pos += 1
 
            print(f' pos={pos}')
            # Put the item there or right after any duplicates.
            while item == vector[pos]:
                pos += 1
            print(f' pos={pos} : swap([{pos}]={vector[pos]},item={item})')
            vector[pos], item = item, vector[pos]
            writes += 1
            print(f' writes={writes} : {vector}, item={item}')
 
    return writes
 
 
if __name__ == '__main__':
    """
    output:
    [0, 1, 2, 2, 2, 2, 1, 9, 3.5, 5, 8, 4, 7, 0, 6]
    Is correctly sorted using cycleSort to
    [0, 0, 1, 1, 2, 2, 2, 2, 3.5, 4, 5, 6, 7, 8, 9]
    Using 10 writes.
    """
    x = [0, 1, 2, 2, 2, 2, 1, 9, 3.5, 5, 8, 4, 7, 0, 6]
    xcopy = x[::]
    writes = cycleSort(xcopy)
    if xcopy != sorted(x):
        print('Wrong order!')
    else:
        print('%r\nIs correctly sorted using cycleSort to'
              '\n%r\nUsing %i writes.' % (x, xcopy, writes))
