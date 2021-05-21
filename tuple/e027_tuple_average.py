def average_tuple_of_tuples(t):
    return [sum(x)/len(x) for x in t]

def average_interleave_tuples(t):
    # web solution: len(x)
    return [sum(x)/len(t) for x in zip(*t)]

T = ((10, 10, 10, 12), (30, 45, 56, 45), (81, 80, 39, 32), (1, 2, 3, 4))
print('tuple', T)
print('moyenne de chaque tuple')
print(average_tuple_of_tuples(T))
print('moyenne par tuples imbriqués (index i pour chaque tuple), i variant de 1 à n')
print(average_interleave_tuples(T))

T = ((1, 1, -5), (30, -15, 56), (81, -60, -39), (-10, 2, 3))
print('tuple', T)
print('moyenne de chaque tuple')
print(average_tuple_of_tuples(T))
print('moyenne par tuples imbriqués (index i pour chaque tuple), i variant de 1 à n')
print(average_interleave_tuples(T))
