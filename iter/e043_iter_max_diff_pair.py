# web solution
from itertools import combinations
from heapq import nlargest

def test(lst):
    print('paires', list(combinations(lst, 2)))
    result = nlargest(1, combinations(lst, 2), key=lambda sub: abs(sub[0] - sub[1]))
    return result

if __name__ == '__main__':
    marks = [32,14,90,10,22,42,31]
    print('liste', marks)
    print("\nmax différence entre 2 éléments:")
    print(test(marks))
