def remove_if_duplicate(ll):
    uniqs = []
    for item in ll:
        if not item in uniqs:
            uniqs.append(item)

    return uniqs

l = [[10, 20], [40], [30, 56, 25], [10, 20], [33], [40]]
print('liste de listes :', l)
print('liste avec éléments uniques :', remove_if_duplicate(l))

# web solution
import itertools
l.sort()
ul = list(x for x, _ in itertools.groupby(l))
print('liste avec éléments uniques :', ul)
