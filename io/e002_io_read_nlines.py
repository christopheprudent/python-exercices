# web solution
def file_read_from_head(fname, nlines):
    from itertools import islice
    with open(fname) as f:
        for line in islice(f, nlines):
            print(line.rstrip("\n"))

file_read_from_head('/home/christophe/Public/sales.txt', 2)
