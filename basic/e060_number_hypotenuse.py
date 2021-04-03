import math
a = float(input('Mesure du côté a du triangle rectangle :'))
b = float(input('Mesure du côté b du triangle rectangle :'))

h = math.sqrt(a**2 + b**2)
print('Hypothénuse d''un triangle rectangle de côtés {} et {} vaut {}'.format(a, b, h))
