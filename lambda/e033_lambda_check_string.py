with_lower = lambda s : any(c.islower() for c in s)
with_upper = lambda s : any(c.isupper() for c in s)
with_digit = lambda s : any(c.isdigit() for c in s)
with_len = lambda s, l : len(s) >= l

s = 'W3resource'
l = 7

if with_lower(s) and with_upper(s) and with_digit(s) and with_len(s, l):
    print('[chaîne OK]')
else:
    print('[chaîne KO]')
    print('lower: ', with_lower(s))
    print('upper: ', with_upper(s))
    print('digit: ', with_digit(s))
    print('len: ', with_len(s, l))

# web solution
def check_string(str1):
    messg = [
    lambda str1: any(x.isupper() for x in str1) or 'String must have 1 upper case character.',
    lambda str1: any(x.islower() for x in str1) or 'String must have 1 lower case character.',
    lambda str1: any(x.isdigit() for x in str1) or 'String must have 1 number.',
    lambda str1: len(str1) >= 7                 or 'String length should be atleast 8.',]
    #print([i(str1) for i in messg])
    result = [x for x in [i(str1) for i in messg] if x != True]
    if not result:
        result.append('Valid string.')
    return result    

while True:
    s = input("Entrez une chaîne (avec au moins 1 minuscule, 1 majuscule, 1 chiffre et de taille minimale de 7): ")
    if len(s) == 0:
        break

    print(check_string(s))
