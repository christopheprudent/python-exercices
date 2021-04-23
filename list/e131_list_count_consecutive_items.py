import itertools

L = [1,2,2,2,4,4,4,5,5,5,5]
print('liste', L)

items=[]
occurs=[]
for x in [list(group) for _, group in itertools.groupby(L)]:
    items.append(x[0])
    occurs.append(len(x))

print('occurences des éléments consécutifs', [items, occurs])
