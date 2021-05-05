L = ['Sum all the items in a list', 'Find the second smallest number in a list']
print('liste', L)
print('bigrams')
print([ (x, y) for l in L for x, y in zip(l.split(), l.split()[1:])])

# web solution
def bigram_sequence(text_lst):
    result = [a for ls in text_lst for a in zip(ls.split(" "), ls.split(" ")[1:])]
    return result

print(bigram_sequence(L))
