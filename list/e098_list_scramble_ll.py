import random

def scramble_list_of_strings(l):
    for i in range(len(l)):
        t = list(l[i])
        random.shuffle(t)
        l[i] = ''.join(t)
    return l

L = ['Python', 'list', 'exercises', 'practice', 'solution']
print('liste:', L)
print('après mélange! :', scramble_list_of_strings(L))

# autre soltion: https://stackoverflow.com/questions/6181304/are-there-any-ways-to-scramble-strings-in-python
print('après mélange! :', [''.join(random.sample(word, len(word))) for word in L])

# web solution
def shuffle_word(text_list):
    text_list = list(text_list)
    random.shuffle(text_list)
    return ''.join(text_list)

print('après mélange! :', [shuffle_word(word) for word in L])
