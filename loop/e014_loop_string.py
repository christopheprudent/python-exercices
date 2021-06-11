s = input('entrez une chaîne de chiffres et de lettres: ')
_digits = _letters = 0
for c in s: 
    if c.isdigit():
        _digits += 1
    elif c.isalpha():
        _letters += 1

print('votre texte contient {} chiffre(s) et {} lettre(s)'.format(_digits, _letters))
