import collections

def groups_key_value(lt):
    d = collections.defaultdict(list)
    for k, v in lt:
        d[k] += [v]

    return d

L = [('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1)]
print('liste', L)
print('après regroupement par clés')
print(groups_key_value(L))
