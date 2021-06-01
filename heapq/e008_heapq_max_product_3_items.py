import heapq
import functools
import operator
import math

L = [12, 74, 9, 50, 61, 41]
print('liste', L)
heapq.heapify(L)
bigs = heapq.nlargest(3, L)
print('les 3 plus grands éléments')
print(bigs)
product = functools.reduce(operator.mul, bigs, 1)
print('plus grand produit de 3 éléments')
print('reduce: ', product)
print('prod:', math.prod(bigs))
