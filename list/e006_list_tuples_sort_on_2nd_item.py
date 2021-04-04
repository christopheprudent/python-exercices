tuples = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
print(sorted(tuples, key= lambda x: x[1]))

# web solution
def last(n): return n[-1]

tuples = [(2, 5, 0), (1, 2, -1), (4, 4, 9), (2, 3, 4), (2, 1, 1)]
print(sorted(tuples, key= lambda x: x[-1]))
print(sorted(tuples, key=last))
