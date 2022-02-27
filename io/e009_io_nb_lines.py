def wc_lines(fname):
    with open(fname) as f:
        lines = f.readlines()
    return len(lines)

# web solution
def file_lengthy(fname):
    with open(fname) as f:
        for i, l in enumerate(f):
            pass
    return i + 1

TEST_FILE='/home/christophe/Public/test.txt'
if __name__ == '__main__':
    print("dev) number of lines", wc_lines(TEST_FILE))
    print("web) number of lines", file_lengthy(TEST_FILE))
