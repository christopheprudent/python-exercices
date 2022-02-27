# web solution
def remove_newlines(fname):
    flist = open(fname).readlines()
    return [s.rstrip('\n') for s in flist]

if __name__ == '__main__':
    TEST_FILE1='/home/christophe/Public/test.txt'
    print(remove_newlines(TEST_FILE1))
