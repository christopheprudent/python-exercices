def remove_words(l, lw):
    return [w for w in l if w not in lw]

L = ['red', 'green', 'blue', 'white', 'black', 'orange']
print('liste', L)
print('après suppression des mots {} : {}'.format(['white', 'orange'], remove_words(L, ['white', 'orange'])))

# web solution
def remove_words2(list1, remove_words):
    for word in list(list1):
        if word in remove_words:
            list1.remove(word)
    return list1

print(remove_words2(L, ['white', 'orange']))
