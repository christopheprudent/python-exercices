import collections

# ne tient pas compte de l'ordre
def is_same_pattern(l, p):
    if len(l) != len(p):
        return False
    cl = collections.Counter(l)
    cp = collections.Counter(p)
    sl = set([v for _, v in cl.items()])
    sp = set([v for _, v in cp.items()])
    return sl == sp

# web solution
def is_samePatterns(colors, patterns):    
    if len(colors) != len(patterns):
        return False    
    sdict = {}
    pset = set()
    sset = set()    
    for i in range(len(patterns)):
        pset.add(patterns[i])
        sset.add(colors[i])
        if patterns[i] not in sdict.keys():
            sdict[patterns[i]] = []

        keys = sdict[patterns[i]]
        keys.append(colors[i])
        print(f' i={i} dict={sdict}')

        #pas besoin!
        #sdict[patterns[i]] = keys

    #print(f' pset={pset} cset={sset}')
    # pset={'b', 'a'} cset={'green', 'red'}
    # dict={'a': ['red'], 'b': ['green', 'greenn']}

    # exclusion si ensembles de taille différente
    if len(pset) != len(sset):
        return False   

    # exclusion si ensembles de valeur différente
    for values in sdict.values():
        for i in range(len(values) - 1):
            if values[i] != values[i+1]:
                return False

    return True

P = ['a', 'b', 'b']

L = ['red', 'green', 'green']
print('liste', L)
print('pattern', P)
print('de même pattern:', 'mine', is_same_pattern(L, P), 'web', is_samePatterns(L, P), '\n')

L = ['red', 'green', 'greenn']
print('liste', L)
print('pattern', P)
print('de même pattern:', 'mine', is_same_pattern(L, P), 'web', is_samePatterns(L, P), '\n')

L = ['green', 'red', 'green']
print('liste', L)
print('pattern', P)
print('de même pattern:', 'mine', is_same_pattern(L, P), 'web', is_samePatterns(L, P))
