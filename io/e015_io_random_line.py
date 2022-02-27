# web solution
import random
def random_line(fname):
    lines = open(fname).read().splitlines()
    return random.choice(lines)

if __name__ == '__main__':
    TEST_FILE1='/home/christophe/Public/test.txt'
    print(random_line(TEST_FILE1))

