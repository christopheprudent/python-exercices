import sys, os, os.path

_PATH='.'
if len(sys.argv)-1:
    _PATH=sys.argv[1] 

if os.path.exists(_PATH):
    _dir, _file = os.path.split(_PATH)
    print('dir: ', _dir)
    print('file: ', _file)

    # web solution
    print('dir: ', os.path.dirname(_PATH))
    print('file: ', os.path.basename(_PATH))

else:
    print('le chemin demandé', _PATH, ' n\'existe pas!')

