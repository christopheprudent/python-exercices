# https://stackoverflow.com/questions/9457832/python-list-rotation
import collections

def rotate(l, n):
    return l[-n:] + l[:-n]

L = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print('liste:', L)

d = collections.deque(L)

d.rotate(-4)
print('rotation à gauche de 4:', list(d))
# reset
d.rotate(4)
#print('liste:', list(d))

d.rotate(-2)
print('rotation à gauche de 2:', list(d))
d.rotate(2)
#print('liste:', list(d))

d.rotate(4)
print('rotation à droite de 4:', list(d))
d.rotate(-4)

d.rotate(2)
print('rotation à droite de 2:', list(d))
d.rotate(-2)
print('liste:', list(d))

print()
print('rotation à gauche de 4:', rotate(L, -4))
print('rotation à gauche de 2:', rotate(L, -2))
print('rotation à droite de 4:', rotate(L, 4))
print('rotation à droite de 2:', rotate(L, 2))
print('liste:', L)
