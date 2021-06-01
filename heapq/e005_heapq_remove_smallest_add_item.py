import heapq

L = [25, 44, 68, 21, 39, 23, 89]
print('liste', L)
heapq.heapify(L)
print('heapq', L)

_min = L[0]
print('valeur MIN', _min)
print('extraction plus petit et ajout de {}'.format(_min))
heapq.heapreplace(L, _min)
print('heapq', L)

_max = heapq.nlargest(1, L)[0]
print('valeur MAX', _max)
print('extraction plus petit et ajout de {}'.format(_max +10))
heapq.heapreplace(L, _max +10)
print('heapq', L)
