# web solution
def list_slice(S, step):
    return [S[i::step] for i in range(step)]

C = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n']
print(list_slice(C,3))
