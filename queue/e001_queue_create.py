# web solution
import queue
q = queue.Queue()

for x in range(4):
    q.put(x)

print("Members of the queue:")
for n in list(q.queue):
    print(n, end=" ")

print("\nSize of the queue:")
print(q.qsize())

