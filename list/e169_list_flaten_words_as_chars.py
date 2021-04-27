def flaten_words_as_chars(l):
    return [y for x in l for y in x]

L = ['red', 'white', 'a', 'b', 'black', 'f']
print('liste', L)
print('séparation de chaque mot en caratères', flaten_words_as_chars(L))
