# web solution
import queue
q = queue.LifoQueue()
for x in range(4):
    print('ajout {} dans la file'.format(x))
    q.put(str(x))

print('liste des éléments de la file')
while not q.empty():
    print(q.get(), end=" ")

print("\n")
