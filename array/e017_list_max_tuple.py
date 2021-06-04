import itertools

def max_tuple_from_list(l):
    """
    l as list of ints
    return (i, j) where i*j is the max
    """
    #max(x*y for x, y in list(itertools.combinations(l, 2)))
    lc = list(itertools.combinations(l, 2))
    slc = sorted(lc, key= lambda x:x[0]*x[1])
    return slc[-1]

# web solution
def max_Product(arr): 
    arr_len = len(arr) 
    if (arr_len < 2): 
        print("No pairs exists") 
        return      
    # Initialize max product pair 
    x = arr[0]; y = arr[1] 

    # Traverse through every possible pair     
    for i in range(0, arr_len): 

        for j in range(i + 1, arr_len): 
            if (arr[i] * arr[j] > x * y): 
                x = arr[i]; y = arr[j] 

    return x,y    

l = [1, 2, 3, 4, 7, 0, 8, 4]
print('liste', l)
print('max x*y :', 'mine=', max_tuple_from_list(l), 'web=', max_Product(l))

l = [0, -1, -2, -4, 5, 0, -6]
print('liste', l)
print('max x*y :', 'mine=', max_tuple_from_list(l), 'web=', max_Product(l))
