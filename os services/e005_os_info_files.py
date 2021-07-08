import os
import sys
import time

path = '.'
print('Path Name ({}):'.format(path))
stat_info = os.stat(path)
print('Size:', stat_info.st_size)
print('Permissions:', oct(stat_info.st_mode))
print('Owner:', stat_info.st_uid)
print('Device:', stat_info.st_dev)
print('Created      :', time.ctime(stat_info.st_ctime))
print('Last modified:', time.ctime(stat_info.st_mtime))
print('Last accessed:', time.ctime(stat_info.st_atime))
