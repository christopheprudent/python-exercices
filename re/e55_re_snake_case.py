# web solution
from re import sub
def snake_case(s):
    """
    a Python program to convert a given string to snake case
    . use re.sub() to replace any - or _ with a space, using the regexp r"(_|-)+"
    . use re.sub() to match all words in the string, str.lower() to lowercase them
    . finally, use str.join() to combine all word using - as the separator
    """
    return '-'.join(
        sub(r"(\s|_|-)+"," ",
            # 2 majuscules, suivies de: [1 majuscule et x minuscules (>=1) et éventuellement de chiffre(s)] ou [séparateur de mot (espace, tab, fin ligne)]
            # 1 majuscule optionnelle et x minuscules (>=1) et éventuellement de chiffre(s)
            # 1 majuscule
            # x chiffre(s)
            sub(r"[A-Z]{2,}(?=[A-Z][a-z]+[0-9]*|\b)|[A-Z]?[a-z]+[0-9]*|[A-Z]|[0-9]+",
                lambda mo: ' ' + mo.group(0).lower(), s
            )
        ).split()
    )
 
print(snake_case('JavaScript'))
print(snake_case('GDScript'))
print(snake_case('BTW...what *do* you call that naming style? snake_case? '))
print(snake_case('OHXx123A*AoneBBTwoCC test33 456'))
