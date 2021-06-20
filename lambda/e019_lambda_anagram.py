L = ['bcda', 'abce', 'cbda', 'cbea', 'adcb', 'aabccd']
w = 'abcd'
print('liste', L)
print('mot', w)
# FIXME tenir compte des occurrences de chaque caractère!
print('anagrammes: ', list(filter(lambda x: all(c in w for c in x), L)))

# web solution
import collections
result = list(filter(lambda x: (collections.Counter(w) == collections.Counter(x)), L)) 
print(result)
