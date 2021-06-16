fibo = lambda x : 0 if x == 0 else 1 if x == 1 else fibo(x-2) + fibo(x-1)

def fibonacci(n):
    _fibo=[]
    for i in range(n):
        _fibo.append(fibo(i))
    return _fibo

# web solution
from functools import reduce
 
# https://www.geeksforgeeks.org/reduce-in-python/

# https://docs.python.org/fr/3/library/functools.html
# def reduce(function, iterable, initializer=None):
#     it = iter(iterable)
#     if initializer is None:
#         value = next(it)
#     else:
#         value = initializer
#     for element in it:
#         value = function(value, element)
#     return value

# v = functools.reduce(lambda x, _: x+[x[-1]+x[-2]], range(3), [0,1])
# [0, 1, 1, 2, 3]
# v = functools.reduce(lambda x, _: x+[x[-1]+x[-2]], range(4), [0,1])
# [0, 1, 1, 2, 3, 5]

fib_series = lambda n: reduce(lambda x, _: x+[x[-1]+x[-2]], range(n-2), [0, 1])
 
n = 2
# [0, 1]
print('{} termes de la suite Fibonacci : {}, {}'.format(n, fibonacci(n), fib_series(n)))

n = 5
# [0, 1, 1, 2, 3]
print('{} termes de la suite Fibonacci : {}, {}'.format(n, fibonacci(n), fib_series(n)))

n = 6
# [0, 1, 1, 2, 3, 5]
print('{} termes de la suite Fibonacci : {}, {}'.format(n, fibonacci(n), fib_series(n)))

n = 9
# [0, 1, 1, 2, 3, 5, 8, 13, 21]
print('{} termes de la suite Fibonacci : {}, {}'.format(n, fibonacci(n), fib_series(n)))
