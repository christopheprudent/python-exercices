def convert_unicode_to_str(l):
    return list(map(str, l))

# web solution
def unicode_to_str(lst):
    result = [str(x) for x in lst]
    return result

L = [u'S001', u'S002', u'S003', u'S004']
print('liste', L)
print('après conversion Unicode en Str')
print(convert_unicode_to_str(L))
print(unicode_to_str(L))
