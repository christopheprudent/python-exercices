# web solution (lambda)
from functools import reduce
 
fib_series = lambda n: reduce(lambda x, _: x+[x[-1]+x[-2]], range(n-2), [0, 1])
 
# web solution (function)
import itertools
def fibonacci_nums(x=0, y=1):
    yield x
    while True:
        yield y
        x, y = y, x + y

n = 6
# [0, 1, 1, 2, 3, 5]
n = 10
list_fibonacci = fib_series(n)
result = list(itertools.islice(fibonacci_nums(), n))
print('{} termes de la suite Fibonacci : {}, {}'.format(n, list_fibonacci, result))
print('valeurs au carré de cette liste')
print(list(map(lambda x: x*x, list_fibonacci)))
