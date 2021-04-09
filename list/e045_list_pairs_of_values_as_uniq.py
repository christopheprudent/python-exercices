def pairs_of_values_as_uniq(lst):
    uniq = []
    for pair in lst:
        if not pair[0] in uniq and not pair[1] in uniq:
            uniq.extend(pair)

    return sorted(uniq)

L = [(1, 2), (3, 4), (1, 2), (5, 6), (7, 8), (1, 2), (3, 4), (3, 4),
 (7, 8), (9, 10)]
print('liste={}'.format(L))
print(pairs_of_values_as_uniq(L))

# web solution
print("Sorted Unique Data:",sorted(set().union(*L)))
