import os

path = '/tmp'
stat_info = os.stat(path)
print('Propriétaire:Groupe=%d:%d' % (stat_info.st_uid, stat_info.st_gid))

fd = os.open(path, os.O_RDONLY)
print('changement propriétaire/groupe')
os.chown(fd, 1000, -1)
os.chown(fd, -1, 1000)
stat_info = os.stat(path)
print('Propriétaire:Groupe=%d:%d' % (stat_info.st_uid, stat_info.st_gid))
os.close(fd)
