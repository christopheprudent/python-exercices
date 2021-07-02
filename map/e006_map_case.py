def to_upper_and_without_dup(s):
    _result = _prev = s[0].upper()
    for c in s[1:]:
        _current = c.upper()
        if _current != _prev:
            _result += _current
        _prev = _current

    return _result

S = 'helllo worldd!'
print('chaîne initiale', S)
print('après mise en majuscule, et sans duplication')
print(to_upper_and_without_dup(S))

# web solution
def change_cases(s):
  return str(s).upper(), str(s).lower()
 
chars = {'a', 'b', 'E', 'f', 'a', 'i', 'o', 'U', 'a'}
print('ensemble des caractères', chars)
print('avec mise en majuscule et en minuscule, sans duplication')
result = map(change_cases, chars)
print(set(result))
