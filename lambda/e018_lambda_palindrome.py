L = ['php', 'w3r', 'Python', 'abcd', 'Java', 'aaa']
print('liste', L)
print('palindromes: ', list(filter(lambda x: x == x[::-1], L)))
