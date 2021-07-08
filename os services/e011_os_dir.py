import sys, os

def dirpath(path):
    with os.scandir(path) as it:
        for entry in it:
            if entry.is_file():
                _type = 'f'
            elif entry.is_dir():
                _type = 'd'
            elif entry.is_symlink():
                _type = 'l'

            print(entry.name)
            if _type == 'd' or _type == 'l':
                dirpath(entry.path)
    
_PATH='.'
if len(sys.argv)-1:
    _PATH=sys.argv[1] 
dirpath(_PATH)

# web solution
for root, dirs, files in os.walk(_PATH):
   print(root)
   for _dir in dirs:
       print(_dir)
   for _file in files:
       print(_file)
