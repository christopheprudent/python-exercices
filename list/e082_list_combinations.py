import itertools
L = [1, 2, 3, 4, 5, 6, 7, 8, 9]
n = 2
print(f'liste {L}')
print('combinaisons de {} éléments'.format(n))
print(list(itertools.combinations(L, n)))

# web solution
def combination(n, n_list):
    if n<=0:
        yield []
        return
    for i in range(len(n_list)):
        c_num = n_list[i:i+1]
        for a_num in combination(n-1, n_list[i+1:]):
            yield c_num + a_num

combs = combination(n, L)
for comb in combs:
    print(comb)
