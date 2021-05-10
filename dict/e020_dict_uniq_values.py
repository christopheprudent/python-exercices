def uniq_values(ld):
    _uniq = []
    for d in ld:
        for v in d.values():
            if v not in _uniq:
                _uniq.append(v)

    return _uniq

L = [{"V":"S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII":"S005"}, {"V":"S009"}, {"VIII":"S007"}] 
print('liste de clé/valeur', L)
print('seulement les valeurs uniques')
print(uniq_values(L))

# web solution
print(set(val for dic in L for val in dic.values()))
