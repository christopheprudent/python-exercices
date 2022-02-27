def combine_lines(file1, file2):
    # https://stackoverflow.com/questions/4617034/how-can-i-open-multiple-files-using-with-open-in-python
    with open(file1, 'r') as a, open(file2, 'r') as b:
        # utiliser itertools.zip_longest() si les 2 fichiers n'ont pas le même nombre de lignes

        # for line1, line2 in zip(a, b):
        for item in zip(a, b):
            print(item)

if __name__ == '__main__':
    TEST_FILE1='/home/christophe/Public/test.txt'
    TEST_FILE2='/home/christophe/Public/test.csv'
    print("dev) combinaison des lignes de 2 fichiers")
    combine_lines(TEST_FILE1, TEST_FILE2)
