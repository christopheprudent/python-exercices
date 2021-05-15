# web solution

#create a tuple
tuplex = (2, 4, 3, 5, 4, 6, 7, 8, 6, 1)
print('tuple', tuplex)
#used tuple[start:stop] the start index is inclusive and the stop index
print('éléments [3, 5[')
_slice = tuplex[3:5]
#is exclusive
print(_slice)
#if the start index isn't defined, is taken from the beg inning of the tuple
print('éléments [0, 6[')
_slice = tuplex[:6]
print(_slice)
#if the end index isn't defined, is taken until the end of the tuple
print('éléments [5, $]')
_slice = tuplex[5:]
print(_slice)
#if neither is defined, returns the full tuple
print('tous les éléments')
_slice = tuplex[:]
print(_slice)
#The indexes can be defined with negative values
print('éléments [-8, -4[')
_slice = tuplex[-8:-4]
print(_slice)

#create another tuple
tuplex = tuple("HELLO WORLD")
print('\n')
print('tuple', tuplex)
#step specify an increment between the elements to cut of the tuple
#tuple[start:stop:step]
print('éléments [2, 9[, par pas de 2')
_slice = tuplex[2:9:2]
print(_slice)
#returns a tuple with a jump every 3 items
print('tous les éléments, par pas de 4')
_slice = tuplex[::4]
print(_slice)
#when step is negative the jump is made back
print('éléments [9, 2[, par pas de -4')
_slice = tuplex[9:2:-4]
print(_slice)
