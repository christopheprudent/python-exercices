def uniq(l):
    _uniq=[]
    for x in l:
        if x in _uniq:
            continue
        _uniq.append(x)

    return _uniq

L = [1,2,3,3,3,3,4,5]
print('liste', L)
print('avec des éléments uniques', uniq(L))
