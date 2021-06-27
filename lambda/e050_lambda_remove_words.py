remove_words = lambda l, r : [x for x in l if not x in r]

# web solution
def remove_words_from_list(list1, remove_words):
    result = list(filter(lambda word: word not in remove_words, list1))
    return result

L = ['orange', 'red', 'green', 'blue', 'white', 'black']
removes = ['orange', 'black']
print('liste', L)
print('sans les mots suivants', removes)
print('mine:', remove_words(L, removes))
print(' web:', remove_words_from_list(L, removes))
