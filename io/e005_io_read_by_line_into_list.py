def file_read_into_list(fname):
    with open(fname) as f:
        lines = [line.rstrip() for line in f]
        # web solution
        # lines = f.readlines()
    return lines

TEST_FILE='/home/christophe/Public/test.txt'
if __name__ == '__main__':
    print("dev) read file line by line (into a list)")
    data = file_read_into_list(TEST_FILE)
    for i, line in enumerate(data):
        print(f'NR={i+1}: {line}')
