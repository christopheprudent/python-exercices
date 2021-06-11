import re

def isint(s):
    return re.search("^[-+]?[0-9]+$", s)

while True:
    text = input('entrez une valeur entière : ')
    if len(text) < 1:
        break
    if isint(text):
        print('OK, bonne saisie')
    else:
        print('tetete, recommencez!')
