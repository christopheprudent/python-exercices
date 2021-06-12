import string

def is_pangram(s):
    _s = s.lower()
    return all(c in _s for c in string.ascii_lowercase)

# web solution
def ispangram(str1, alphabet=string.ascii_lowercase):
    alphaset = set(alphabet)
    return alphaset <= set(str1.lower())

print('tests de pangram')
while True:
    s = input('entrez une chaîne de caractères : ')
    if len(s) == 0:
        break

    if is_pangram(s):
        print(' votre chaîne est un pangram')
    if ispangram(s):
        print(' votre chaîne est un pangram')
