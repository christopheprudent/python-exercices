# web solution
import queue
p = queue.Queue()
q = queue.Queue()
for x in range(4):
    q.put(x)
print('queue p, vide: ', p.empty())
print('queue q, vide: ', q.empty())
