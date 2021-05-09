D = {'data1':100,'data2':-54,'data3':247}
print('dictionnaire', D)
print('multiplication des valeurs')
_mul = 1
for x in D.values():
    _mul *= x
print(_mul)

# web solution
_mul = 1
for key in D: 
    _mul=_mul * D[key]
print(_mul)
