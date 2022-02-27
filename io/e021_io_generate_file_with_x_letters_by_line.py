# web solution
import string
def letters_file_line(fn, n):
   with open(fn, "w") as f:
       alphabet = string.ascii_uppercase
       letters = [alphabet[i:i + n] + "\n" for i in range(0, len(alphabet), n)]
       f.writelines(letters)

if __name__ == '__main__':
    n = 3
    print('dev) génération fichier avec %d lettres par ligne' % n) 
    FOLDER='/home/christophe/Public'
    FILE='letters.txt'
    letters_file_line(FOLDER + '/' + FILE, n)

    print(open(FOLDER + '/' + FILE, 'r').read())
