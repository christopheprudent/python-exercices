def remove_dup_words(l):
    return list(set(l))

# web solution (preserve order)
def unique_list(l):
    temp = []
    for x in l:
        if x not in temp:
            temp.append(x)
    return temp

L = ['Python', 'Exercises', 'Practice', 'Solution', 'Exercises']
print('liste', L)
print('sans doublon:', remove_dup_words(L))
print('sans doublon (même ordre):', unique_list(L))
