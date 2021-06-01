# web solution
import heapq
from collections import Counter
def reorganizeString(S):
    print('chaîne', S)
    ctr = Counter(S)
    heap = [(-value, key) for key, value in ctr.items()]
    heapq.heapify(heap)
    if (-heap[0][0]) * 2 > len(S) + 1: 
        return ""
    ans = []
    while len(heap) >= 2:
        print(' heap', heap)
        nct1, char1 = heapq.heappop(heap)
        nct2, char2 = heapq.heappop(heap)
        print(f' n1={nct1}, c1={char1}')
        print(f' n2={nct2}, c2={char2}')
        print(' heap', heap)
        ans.extend([char1, char2])
        print(' solution', ans)
        if nct1 + 1: heapq.heappush(heap, (nct1 + 1, char1))
        if nct2 + 1: heapq.heappush(heap, (nct2 + 1, char2))
        print(' heap', heap)
    return "".join(ans) + (heap[0][1] if heap else "")

print(" " + reorganizeString("aab"))
print(" " + reorganizeString("abc"))
print(" " + reorganizeString("aabb"))
print(" " + reorganizeString("abccdd"))
