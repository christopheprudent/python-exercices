print('transformation en dictionnaire')

T = 1, 2, 'a', 1, 3, 'A', 0, 'A', -1, 'A'
print('tuple', T)
print({x:y for x,y in zip(T[::2], T[1::2])})

# web solution
#create a tuple
tuplex = ((2, "w"),(3, "r"))
print()
print('tuple', tuplex)
print(dict((y, x) for x, y in tuplex))
