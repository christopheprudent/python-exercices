# https://fr.wikipedia.org/wiki/Refroidissement_%C3%A9olien

#import math

v = float(input('Entrer la vitesse du vent (en km/h) : '))
t = float(input(' et la température de l\'air (en °Celsius) : '))

"""
t en °Celsius, v en km/h
Rc = 13.12 + 0.6215 * t + (0.3965 * t - 11.37) * v ** 0.16

t en °Fahrenheit, v en mph
Rf = 35.74 + 0.6215 * t + (0.4275 * t - 35.75) * v ** 0.16
"""

wci = 13.12 + 0.6215 * t + (0.3965 * t - 11.37) * (v ** 0.16)
print('dev) refroidissement éolien', wci)
