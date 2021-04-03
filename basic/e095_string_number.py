#str = 'a123'
#str = '123.1'
str = '123,1'
try:
    i = float(str)
except (ValueError, TypeError):
    print('\nNot numeric')
print()

