import re

def snake_to_camel_upper(under_first_letter):
    #print(under_first_letter.group(0)[1].upper())
    return under_first_letter.group(0)[1].upper()

def snake_to_camel(text):
    return re.sub('(_[a-z0-9])', snake_to_camel_upper, text)

# web solution
def snake_to_camel2(word):
    return ''.join(x.capitalize() or '_' for x in word.split('_'))

snake_case = 'snake_case_string'
print('dev) conversion "%s" de snake_case en camelCase : %s' % (snake_case, snake_to_camel(snake_case)))
print('web) conversion "%s" de snake_case en camelCase : %s' % (snake_case, snake_to_camel2(snake_case)))
