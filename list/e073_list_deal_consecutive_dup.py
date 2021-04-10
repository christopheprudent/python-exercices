def remove_consecutive_dup(l):
    if not l: return l
    nl = [l[0]]
    for i in range(1, len(l)):
        print(f'i={i} p={l[i-1]} c={l[i]}')
        if l[i] != l[i-1]:
            nl.append(l[i])

    return nl

L = [0, 0, 1, 2, 3, 4, 4, 5, 6, 6, 6, 7, 8, 9, 4, 4]
print('liste: ', L)
print('sans élément dupliqué: ', remove_consecutive_dup(L)) 

# web solutions
from itertools import groupby, repeat
def compress(l_nums):
    return [key for key, _ in groupby(l_nums)] 
# pack consecutive duplicates
def pack(l_nums):
    return [list(group) for _, group in groupby(l_nums)] 
# list reflecting the run-length encoding
def pack_len(l):
    return [[len(list(group)), key] for key, group in groupby(l)]
# run-length encoding only if multiple dups!
def pack_len_only_multiple(l):
    def check_multiple(e):
        if len(e)>1: return [len(e), e[0]]
        else: return e[0]
    return [check_multiple(list(group)) for _, group in groupby(l)]
# pack decode
def pack_decode(p):
    n = []
    for x in p:
        if isinstance(x, list):
            for y in repeat(x[1], x[0]): n.append(y)
        else: n.append(x)

    return n
# decode web solution
def pack_decode2(alist):
    def aux(g):
        if isinstance(g, list):
            return [(g[1], range(g[0]))]
        else:
            return [(g, [0])]
    return [x for g in alist for x, R in aux(g) for i in R]

print()
print('sans élément dupliqué')
print(compress(L))
print('avec groupement des éléments')
print(pack(L))
print('avec groupement (nombre, élément)')
print(pack_len(L))
print('avec groupement (nombre, élément) seulement pour les éléments mutiples')
print(pack_len_only_multiple(L))
print('décodage à partir du groupement')
print(pack_decode([[2, 1], 2, 3, [2, 4], 5, 1]))
print(pack_decode2([[2, 1], 2, 3, [2, 4], 5, 1]))
