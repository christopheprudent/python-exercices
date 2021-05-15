def remove_empty_typle(lt):
    return [t for t in lt if t]

L = [(), (), ('',), ('a', 'b'), ('a', 'b', 'c'), ('d')]
print('liste', L)
print('suppression des tuples vides')
print(remove_empty_typle(L))
