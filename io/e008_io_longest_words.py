# web solution
def longest_word(filename):
    with open(filename, 'r') as infile:
              words = infile.read().split()
    max_len = len(max(words, key=len))
    return [word for word in words if len(word) == max_len]

TEST_FILE='/home/christophe/Public/test.txt'
if __name__ == '__main__':
    print(longest_word(TEST_FILE))

