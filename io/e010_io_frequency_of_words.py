# web solution
from collections import Counter
def word_count(fname):
    with open(fname) as f:
        return Counter(f.read().split())

TEST_FILE='/home/christophe/Public/test.txt'
if __name__ == '__main__':
    print("web) fréquence des mots du fichier", word_count(TEST_FILE))
