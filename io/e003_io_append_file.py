def append_file(fname, data):
    with open(fname, 'a') as f:
        f.write(data + '\n')

TEST_FILE='/home/christophe/Public/test.txt'
if __name__ == '__main__':
    append_file(TEST_FILE, '1 A')
    append_file(TEST_FILE, '22 BB')
    append_file(TEST_FILE, '333 CCC')

    with open(TEST_FILE, 'r') as f:
        print(f.read())
