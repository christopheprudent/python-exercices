import string
import pathlib
import glob
def generate_files_one_for_each_letter(folder):
    for _l in string.ascii_uppercase:
        pathlib.Path(folder + '/' + _l + '.txt').touch() 

if __name__ == '__main__':
    print('dev) génération 26 fichiers')
    FOLDER='/home/christophe/Public'
    generate_files_one_for_each_letter(FOLDER)
    print(glob.glob(FOLDER + '/?.txt'))
