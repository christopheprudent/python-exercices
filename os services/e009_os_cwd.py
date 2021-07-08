import os

_cwd = os.getcwd()
print('chemin courant: ', _cwd)
print('remontée dans le dossier parent')
# os.pardir()
os.chdir(_cwd + '/..')
_cwd = os.getcwd()
print('chemin courant: ', _cwd)
