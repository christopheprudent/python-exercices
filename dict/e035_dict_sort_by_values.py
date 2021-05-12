D = {'Math':81, 'Physics':83, 'Chemistry':87}
print('dictionnaire', D)
print('trié par valeurs')
print('solution 1: lambda')
print(sorted(D.items(), key=lambda x:x[1]))
import operator
print('solution 2: itemgetter')
print(sorted(D.items(), key=operator.itemgetter(1)))

# web solution
import collections
print('solution 3: Counter.most_common')
x = collections.Counter(D)
print(x.most_common())
