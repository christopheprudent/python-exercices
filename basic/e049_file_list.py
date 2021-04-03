from os import listdir
from os.path import isfile, join
files_list = [f for f in listdir('/home/christophe/Devel/python/basic') if isfile(join('/home/christophe/Devel/python/basic', f))]
print(files_list);

