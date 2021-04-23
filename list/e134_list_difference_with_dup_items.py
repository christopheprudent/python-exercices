# https://stackoverflow.com/questions/8106227/difference-between-two-lists-with-duplicates-in-python
from collections import Counter

def list_difference(a, b):
    count = Counter(a) # count items in a
    count.subtract(b)  # subtract items that are in b
    diff = []
    for x in a:
        if count[x] > 0:
           count[x] -= 1
           diff.append(x)
    return diff

# web solution
def list_difference2(l1,l2):
    result = list(l1)
    for el in l2:
        result.remove(el)
    return result

# other one
from typing import Sequence
import itertools

def duplicates_difference(a: Sequence, b: Sequence) -> Counter:
    """
    >>> duplicates_difference([1,2],[1,2,2,3])
    Counter({2: 1, 3: 1})
    """
    shorter, longer = sorted([a, b], key=len)
    return Counter(longer) - Counter(shorter)

L1 = [1, 1, 2, 3, 3, 4, 4, 5, 6, 7]
L2 = [1, 1, 2, 4, 5, 6]
print('liste1', L1)
print('liste2', L2)
print('liste1 - liste2')
print(list_difference(L1, L2))
print(list_difference2(L1, L2))
diff_counter = duplicates_difference(L1, L2)
diff_list = list(itertools.chain.from_iterable(itertools.repeat(x, n) for x, n in diff_counter.items()))
print(diff_list)
