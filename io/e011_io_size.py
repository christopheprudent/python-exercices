def size_of_file(fname):
    with open(fname) as f:
        f.seek(0, 2)
        sz = f.tell()
    return sz

# web solution
def file_size(fname):
    import os
    statinfo = os.stat(fname)
    return statinfo.st_size

TEST_FILE='/home/christophe/Public/test.txt'
if __name__ == '__main__':
    print("dev) taille du fichier", size_of_file(TEST_FILE))
    print("web) taille du fichier", file_size(TEST_FILE))
