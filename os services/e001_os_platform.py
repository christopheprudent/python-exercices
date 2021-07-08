import platform, os

print('nom système d\'exploitation')
print('plateforme', platform.platform())
print('système', platform.system(), os.uname())
print('nom', os.name)
print('pwd', os.getcwd())
print('liste des fichiers')
print(os.listdir('.'))

print('tentative lecture fichier')
try:
   filename = 'abc.txt'
   f = open(filename, 'r')
   text = f.read()
   f.close()
except IOError:
   print('Non accessible (ou erreur de lecture): ' + filename)
