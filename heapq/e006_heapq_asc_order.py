import heapq

L = [18, 14, 10, 9, 8, 7, 9, 3, 2, 4, 1]
print('liste', L)
heapq.heapify(L)
print('en ordre croissant (à l\'aide de heapq)')
print(heapq.nsmallest(len(L), L))

# web solution
print([heapq.heappop(L) for i in range(len(L))])
