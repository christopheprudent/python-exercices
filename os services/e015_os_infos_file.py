import os, sys, time

_PATH=__file__
if len(sys.argv)-1:
    _PATH=sys.argv[1] 

# web solution

fd = os.open(_PATH, os.O_RDWR)
info = os.fstat(fd)
print (f"ID of device containing it: {info.st_dev}")
print (f"              Inode number: {info.st_ino}")
print (f"                Protection: {info.st_mode}")
print (f"      Number of hard links: {info.st_nlink}")
print (f"          User ID of owner: {info.st_uid}")
print (f"         Group ID of owner: {info.st_gid}")
print (f"      Total size, in bytes: {info.st_size}")
print (f"       Time of last access: (EPOCH-{info.st_atime}) {time.ctime(info.st_atime)}")
print (f" Time of last modification: (EPOCH-{info.st_mtime}) {time.ctime(info.st_mtime)}")
print (f"Time of last status change: (EPOCH-{info.st_ctime}) {time.ctime(info.st_ctime)}")
os.close(fd)
