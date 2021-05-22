from collections import Counter, OrderedDict

# web solution
class OrderedCounter(Counter, OrderedDict):
   pass

n = int(input('entrez le nombre de mots à saisir: '))
c = Counter()
word_array = []
for i in range(n):
    s = input('entrer un mot: ').strip()
    c[s] += 1
    word_array.append(s)

print('vous avez saisi {} mots différents'.format(len(c)))
word_ctr = OrderedCounter(word_array)
print(len(word_ctr))

print('avec leurs occurences: ', c)
print()
print('avec leurs occurences, dans leur ordre de saisie')
for word in word_ctr:
   print(word, word_ctr[word], end=' ')
print()
