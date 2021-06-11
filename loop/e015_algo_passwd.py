def valid_passwd(p):
    if len(p) < 6 or len(p) > 16:
        return False

    if not any(c.islower() for c in p):
        return False

    if not any(c.isupper() for c in p):
        return False

    if not any(c.isdigit() for c in p):
        return False

    if not any(c in ['$', '#', '@'] for c in p):
        return False

    return True

print('Tests validité de mots de passe')
#for pw in ['test', 'Test', 'Test0', 'Test1$', '00aaBB#', '    3@', 'TEST_KO_CAR_TROP_LONG', 'TEST_0_a_$_MAIS_TROP_LONG']:
#    print('mot de passe: ({}) de validité : {}'.format(pw, valid_passwd(pw)))

# web solution
import re
p= input("Input your password")
x = True
while x:  
    if (len(p)<6 or len(p)>12):
        break
    elif not re.search("[a-z]",p):
        break
    elif not re.search("[0-9]",p):
        break
    elif not re.search("[A-Z]",p):
        break
    elif not re.search("[$#@]",p):
        break
    elif re.search("\s",p):
        break
    else:
        print("Valid Password")
        x=False
        break

if x:
    print("Not a Valid Password")
