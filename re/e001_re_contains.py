import re

# web solution
def is_allowed_specific_char(string):
    charRe = re.compile(r'[^a-zA-Z0-9]')
    string = charRe.search(string)
    return not bool(string)

while True:
    _set = 'a-zA-Z0-9'
    _test = input('Entrez une chaîne, dont toutes les lettres appartiennent à [%s] : ' % _set)
    if len(_test) == 0:
        break

    # FIXME: souci avec ?, exemple: ok? est accepté, mais pas ?
    if re.match(r'[' + _set + ']+', _test) != None:
        print('ok')
    else:
        print('ko')

    print(is_allowed_specific_char(_test))
