import collections

def grouping_key_values(l):
    d = collections.defaultdict(list)
    for (k,v) in l:
        d[k].append(v)

    return d

# web solution
def grouping_dictionary(l):
    result = {}
    for k, v in l:
         result.setdefault(k, []).append(v)
    return result

L = [('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1)]
print('liste', L)
print('en groupant les clés')
print(grouping_key_values(L))
print(grouping_dictionary(L))
