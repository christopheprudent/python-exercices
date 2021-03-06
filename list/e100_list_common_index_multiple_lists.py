def common_index_lists(*lists):
    m = min(len(l) for l in lists)
    idx = []
    # colonne
    for j in range(m):
        ok = True
        # ligne
        for i in range(len(lists)-1):
            print(f'i={i} j={j} l(i)={lists[i][j]} l(i+1)={lists[i+1][j]}')
            if lists[i][j] != lists[i+1][j]:
                ok = False
                break
        if ok:
            idx.append(j)

    return [ lists[0][x] for x in idx ]
            
# les colonnes (2, 6) sont identiques : [2, 7]
print(common_index_lists(
      [1, 1, 2, 4, 5, 6, 7]
    , [0, 1, 2, 3, 4, 5, 7] 
    , [0, 1, 2, 3, 4, 5, 7] 
    , [6, 2, 2, 3, 4, 5, 7] 
))
