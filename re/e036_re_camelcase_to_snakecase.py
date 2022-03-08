import re

def camel_to_snake(text):
    m = re.findall(r'([A-Z])?([a-z0-9]+)', camelCase)
    #[('', 'camel'), ('C', 'ase'), ('S', 'tring')]
    snake_case = ''
    for u, w in m:
        if u:
            snake_case += u.lower()
        if w:
            snake_case += w + '_'
    return snake_case[:-1]

# web solution
def camel_to_snake2(text):
    #[('l', 'Case')]
    #print(re.findall('(.)([A-Z][a-z]+)', text))
    str1 = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', text)
    #camel_CaseString
    #print(str1)
    #print(re.findall('([a-z0-9])([A-Z])', str1))
    return re.sub('([a-z0-9])([A-Z])', r'\1_\2', str1).lower()

camelCase = 'camelCaseString'
print('dev) conversion "%s" de camelCase en snake_case : %s' % (camelCase, camel_to_snake(camelCase)))
print('web) conversion "%s" de camelCase en snake_case : %s' % (camelCase, camel_to_snake2(camelCase)))
