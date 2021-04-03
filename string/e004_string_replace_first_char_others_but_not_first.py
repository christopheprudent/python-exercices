def replace_first_others(s, r='$'):
  return ''.join([ r if i>0 and c == s[0] else c for i, c in enumerate(s) ])

# web solution
def change_char(str1):
  char = str1[0]
  str1 = str1.replace(char, '$')
  str1 = char + str1[1:]

  return str1

print(replace_first_others('restart'))
print(replace_first_others('hello, how do you do? where are you?'))

print(change_char('restart'))
