def constraints_string(s, min_len=8):
    messg = []
    if not any(x.isupper() for x in s):
        messg.append('String must have 1 upper case character.')
    if not any(x.islower() for x in s):
        messg.append('String must have 1 lower case character.')
    if not any(x.isdigit() for x in s):
        messg.append('String must have 1 number.')
    if len(s) < min_len:
        messg.append('String length should be atleast {}.'.format(min_len))
    if not messg:
        messg.append('Valid string.')
    return messg
    
s = input("Input the string: ")
print(constraints_string(s))

