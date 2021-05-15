import collections

def convert_list_of_tuples_to_dict(l):
    d = collections.defaultdict(list)
    for k, v in l:
        d[k].append(v)
            
    return d

# web solution
def convert_to_dict(lt):
    d = {}
    for a, b in lt:
        d.setdefault(a, []).append(b)

    return d

L = [("x", 1), ("x", 2), ("x", 3), ("y", 1), ("y", 2), ("z", 1)]
print('liste', L)
print('conversion en dictionnaire')
print(convert_list_of_tuples_to_dict(L))
print(convert_to_dict(L))
