import re
ip = "216.08.094.196"
ip_tr = re.sub('\.[0]*', '.', ip)
print('IP %s transformée (sans 0 en préfixe) %s' % (ip, ip_tr))
ip = "016.08.094.196"
ip_tr = re.sub('^[0]*', '', re.sub('\.[0]*', '.', ip))
print('IP %s transformée (sans 0 en préfixe) %s' % (ip, ip_tr))
