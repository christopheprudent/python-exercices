import sys, os, stat

_FILES_ONLY=True
_DIRS_ONLY=False
_DIRS_FILES=False
_PATH='.'

if len(sys.argv)-1:
    if '--files_only' in sys.argv: 
        _FILES_ONLY=True
        _DIRS_ONLY=_DIRS_FILES=False
    elif '--dirs_only' in sys.argv: 
        _DIRS_ONLY=True
        _FILES_ONLY=_DIRS_FILES=False
    elif '--dirs_files' in sys.argv: 
        _DIRS_FILES=True
        _FILES_ONLY=_DIRS_only=False

    _pi = sys.argv.index('--path')
    if _pi and (len(sys.argv) > _pi):
        _PATH=sys.argv[_pi +1] 

perm_masks=[
    stat.S_IRUSR
  , stat.S_IWUSR
  , stat.S_IXUSR
  , stat.S_IRGRP
  , stat.S_IWGRP
  , stat.S_IXGRP
  , stat.S_IROTH
  , stat.S_IWOTH
  , stat.S_IXOTH
]

perm_prints=[
    'r'
  , 'w'
  , 'x'
  , 'r'
  , 'w'
  , 'x'
  , 'r'
  , 'w'
  , 'x'
]

with os.scandir(_PATH) as it:
    for entry in it:
        _print=False
        if (_FILES_ONLY or _DIRS_FILES) and entry.is_file():
            _print=True
        if (_DIRS_ONLY or _DIRS_FILES) and entry.is_dir():
            _print=True

        if _print:
            print(entry.name)
            _stat=entry.stat()
            #print('permissions:', 'u=', _stat.st_mode&stat.S_IRWXU, 'g=', _stat.st_mode&stat.S_IRWXG, 'o=', _stat.st_mode&stat.S_IRWXO)
            _perm=''
            for i in range(len(perm_masks)):
                if _stat.st_mode & perm_masks[i]:
                    _perm+=perm_prints[i]
                else:
                    _perm+='-' 
            print('permissions:', _perm)
