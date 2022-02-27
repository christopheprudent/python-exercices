import re

def nof_words(fname):
    _lines = open(fname).readlines()
    _nof = 0
    
    for _line in _lines:
        # seulement pour espace comme séparateur
        #_nof += len(_line.split())

        _nof += len(re.split(r'[ ,;]', _line))

    return _nof

if __name__ == '__main__':
    TEST_FILE1='/home/christophe/Public/test.txt'
    TEST_FILE2='/home/christophe/Public/test.csv'
    print('dev) nombre de mots', nof_words(TEST_FILE2))
