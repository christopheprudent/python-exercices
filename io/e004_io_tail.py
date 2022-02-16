# web solution
import sys
import os

def file_read_from_tail(fname,lines):
    bufsize = 8192
    fsize = os.stat(fname).st_size
    iter = 0
    with open(fname) as f:
        if bufsize > fsize:
            bufsize = fsize-1
            data = []
            while True:
                iter +=1
                f.seek(fsize-bufsize*iter)
                data.extend(f.readlines())
                if len(data) >= lines or f.tell() == 0:
                    print(''.join(data[-lines:]))
                    break

# others: https://stackoverflow.com/questions/136168/get-last-n-lines-of-a-file-similar-to-tail
from collections import deque
def tail(filename, n=10):
    with open(filename) as f:
        return deque(f, n)

def tail2(f, window=20):
    """
    Returns the last `window` lines of file `f` as a list.
    f - a byte file-like object
    """
    if window == 0:
        return []
    BUFSIZ = 1024
    # seek takes 2 parameters, an offset (how many bytes) and whence which describes from where to seek (start:0, current:1, end:2=io.SEEK_END) 
    f.seek(0, 2)
    bytes = f.tell()
    size = window + 1
    block = -1
    data = []
    while size > 0 and bytes > 0:
        if bytes - BUFSIZ > 0:
            # Seek back one whole BUFSIZ
            f.seek(block * BUFSIZ, 2)
            # read BUFFER
            data.insert(0, f.read(BUFSIZ))
        else:
            # file too small, start from begining
            f.seek(0,0)
            # only read what was not read
            data.insert(0, f.read(bytes))
        linesFound = data[0].count('\n')
        size -= linesFound
        bytes -= BUFSIZ
        block -= 1
    return ''.join(data).splitlines()[-window:]

TEST_FILE='/home/christophe/Public/test.txt'
if __name__ == '__main__':
    print("web) tail w/ algo seek")
    file_read_from_tail(TEST_FILE, 3)

    print("web) tail w/ deque")
    lines = tail(TEST_FILE, 6)
    for line in lines:
        print(line.rstrip('\n'))

    print("web) another tail w/ seek")
    with open(TEST_FILE) as f:
        lines = tail2(f, 6)
    for line in lines:
        print(line.rstrip('\n'))
