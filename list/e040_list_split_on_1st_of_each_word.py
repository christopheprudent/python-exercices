from collections import defaultdict

def split_on_1st_of_each_word(words):
    split_words = defaultdict(list)
    for word in words:
        split_words[word[:1]].append(word)

    return split_words

words_list = ['be','have','do','say','get','make','go','know','take','see','come','think',
     'look','want','give','use','find','tell','ask','work','seem','feel','leave','call']

# output: defaultdict(<class 'list'>, {'b': ['be'], 'h': ['have'], 'd': ['do'], 's': ['say', 'see', 'seem'], 'g': ['get', 'go', 'give'], 'm': ['make'], 'k': ['know'], 't': ['take', 'think', 'tell'], 'c': ['come', 'call'], 'l': ['look', 'leave'], 'w': ['want', 'work'], 'u': ['use'], 'f': ['find', 'feel'], 'a': ['ask']})
print(split_on_1st_of_each_word(words_list))

# web solution
from itertools import groupby
from operator import itemgetter

for letter, words in groupby(sorted(words_list), key=itemgetter(0)):
    print(letter)
    for word in words:
        print('\t' + word)

