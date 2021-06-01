import heapq

def k_tuples_from_2_arrays(k, l1, l2):
    if len(l1) < k or len(l2) < k:
        return None

    return [(heapq.heappop(l1), heapq.heappop(l2)) for _ in range(k)]

# web solution
def k_Smallest_Pairs(nums1, nums2, k):
    queue = []
    def push(i, j):
        if i < len(nums1) and j < len(nums2):
            heapq.heappush(queue, [nums1[i] + nums2[j], i, j])
    push(0, 0)
    pairs = []
    while queue and len(pairs) < k:
        print(f'queue={queue}')
        _, i, j = heapq.heappop(queue)
        print(f'i={i} j={j}')
        pairs.append([nums1[i], nums2[j]])
        print(f'pairs={pairs}')
        push(i, j + 1)
        if j == 0:
            push(i + 1, 0)
    print(f'queue={queue}')
    return pairs

L1 = [0, 1, 2, 3]
L2 = [10, 11, 12, 13]
print('liste1', L1)
print('liste2', L2)
k = 4
print('k={} tuples(u, v), u \u03F5 L1 et v \u03F5 L2'.format(k))
print(k_tuples_from_2_arrays(k, L1, L2))
L1 = [0, 1, 2, 3]
L2 = [10, 11, 12, 13]
print(k_Smallest_Pairs(L1, L2, k))
