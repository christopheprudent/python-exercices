# web solution
def func_compute(n):
    return lambda x : x * n

n = 15
for m in range(2, 6):
    result = func_compute(m)
    print("%d*%d=%d" % (m, n, result(n)))
