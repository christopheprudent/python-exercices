import os

print('PPID:', os.getppid())
print('PID:', os.getpid())
print('EUID:', os.geteuid())
_euid = int(input('entrez une nouvelle valeur de EUID: '))
os.seteuid(_euid)
# 65534 (nobody), mais pas assez de privilèges: PermissionError: [Errno 1] Operation not permitted
# lancement en root: sudo python3 e008_os_ids.py, OK
print('EUID:', os.geteuid())
