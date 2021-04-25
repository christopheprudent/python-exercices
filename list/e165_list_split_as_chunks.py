# https://stackoverflow.com/questions/312443/how-do-you-split-a-list-into-evenly-sized-chunks
def chunks(lst, n):
    """Yield successive n-sized chunks from lst."""
    for i in range(0, len(lst), n):
        yield lst[i:i + n]

L = [12, 45, 23, 67, 78, 90, 45, 32, 100, 76, 38, 62, 73, 29, 83]
print('liste', L)
print('composé en blocs de 3 éléments', list(chunks(L, 3)))
print('composé en blocs de 4 éléments', list(chunks(L, 4)))
print('composé en blocs de 5 éléments', list(chunks(L, 5)))

print()

# web solution
def split_list(lst, n):
    result = list((lst[i:i+n] for i in range(0, len(lst), n)))
    return result

print('composé en blocs de 3 éléments', split_list(L, 3))
print('composé en blocs de 4 éléments', split_list(L, 4))
print('composé en blocs de 5 éléments', split_list(L, 5))
