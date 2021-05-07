L = ['red', 'green', 'white', 'black']
print('liste', L)
print('en ordre inverse')
print(L[::-1])
print('en ordre inverse, avec index original')
for i, x in enumerate(L[::-1]):
    print('{} {}'.format(len(L) -i-1, x))

# web solution
for i, el in reversed(list(enumerate(L))):
    print(i, el)
