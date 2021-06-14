import re
check_number = lambda s : all(x.isdigit() for x in s)

#FIXME accepte ..10 !
check_number2 = lambda s : re.search(r"[-+]?\d*\.?\d+", s)

#FIXME
#entrez un nombre entier: ..2
#erreur de saisie!
#entrez un nombre entier: 1..2
numeric_const_pattern = r"""
[-+]? # optional sign
(?:
    (?: \d* \. \d+ ) # .1 .12 .123 etc 9.1 etc 98.1 etc
    |
    (?: \d+ \.? ) # 1. 12. 123. etc 1 12 123 etc
)
# followed by optional exponent part if desired
(?: [Ee] [+-]? \d+ ) ?
"""
rx = re.compile(numeric_const_pattern, re.VERBOSE)
check_number3 = lambda s : rx.match(s)


while True:
    n = input('entrez un nombre entier: ')
    if len(n) == 0:
        break

#    if not check_number(n):
#        print('check_number: erreur de saisie!')

    if not check_number3(n):
        print('erreur de saisie!')
