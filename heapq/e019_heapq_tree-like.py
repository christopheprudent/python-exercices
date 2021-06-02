# web solution
import math
from io import StringIO
#source https://bit.ly/38HXSoU
def show_tree(tree, total_width=60, fill=' '):
    """Pretty-print a tree.
    total_width depends on your input size"""
    output = StringIO()
    last_row = -1
    for i, n in enumerate(tree):
        if i:
            row = int(math.floor(math.log(i+1, 2)))
        else:
            row = 0
        if row != last_row:
            output.write('\n')
        columns = 2**row
        col_width = int(math.floor((total_width * 1.0) / columns))
        print(f' i={i} n={n} row={row} cols={columns} col_width={col_width}')
        output.write(str(n).center(col_width, fill))
        last_row = row
    print (output.getvalue())
    print ('-' * total_width)
    return

#test
import heapq
heap = []
heapq.heappush(heap, 1)
heapq.heappush(heap, 2)
heapq.heappush(heap, 3)
heapq.heappush(heap, 4)
heapq.heappush(heap, 7)
heapq.heappush(heap, 9)
heapq.heappush(heap, 10)
heapq.heappush(heap, 8)
heapq.heappush(heap, 16)
heapq.heappush(heap, 14)
show_tree(heap)

heap = []
heapq.heappush(heap, (1, 'one', 2))
heapq.heappush(heap, (1, 'one', 3))
heapq.heappush(heap, (1, 'one', 1))
heapq.heappush(heap, (1, 'one', 4))
heapq.heappush(heap, (1, 'one', 5))
heapq.heappush(heap, (1, 'one', 6))
heapq.heappush(heap, (1, 'one', 89))
show_tree(heap)
