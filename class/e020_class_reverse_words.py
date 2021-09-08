import re

class my_solution:
    def reverse_words(self, sentence):
        _words = re.split(r'[ ]+', sentence)
        # my solution
        for i in reversed(range(len(_words))):
            print(_words[i], end=' ')
        print()

        # web solution
        print(' '.join(reversed(_words)))

my = my_solution()
my.reverse_words('Hello World !')
my.reverse_words('Hello .py')
