import time, os

filestat = os.stat(__file__)
date = time.localtime(filestat.st_mtime)
print('fichier %s dernièrement modifié le %02d/%02d/%4d à %02d:%02d:%02d' % (__file__, date[2], date[1], date[0], date[3], date[4], date[5]))
