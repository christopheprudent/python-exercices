# web solution
from itertools import zip_longest, chain, tee
def replace2copy(lst):
    lst1, lst2 = tee(iter(lst), 2)
    return list(chain.from_iterable(zip_longest(lst[1::2], lst[::2])))

n = [0,1,2,3,4,5,6]
print(replace2copy(n))

if len(n) % 2:
    n.append(None)

nn = []
for i in range(0, len(n), 2):
    nn.append(n[i+1])
    nn.append(n[i])

print(nn)
