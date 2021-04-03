import os
_input = input('Entrez le nom d''un fichier avec son chemin :')
_base = os.path.basename(_input)
_file = os.path.splitext(_base)
print('Le fichier', _file[0], 'a pour extension', _file[1])
