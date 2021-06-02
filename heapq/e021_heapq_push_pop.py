import heapq

heap = []
heapq.heappush(heap, ('V', 1))
heapq.heappush(heap, ('V', 2))
heapq.heappush(heap, ('V', 3))

# web solution
for a in heap:
	print(a)

for _ in range(len(heap)):
    print(heapq.heappop(heap))
