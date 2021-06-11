# web: https://www.metric-conversions.org/temperature/fahrenheit-to-celsius.htm
# C = (5/9) * (F - 32)

def celsius2fahrenheit(d):
    return ((d*1.8) + 32)

def fahrenheit2celsius(d):
    return ((d - 32)/1.8)

t = 60
print('{}°C = {}°F'.format(t, celsius2fahrenheit(t)))
t = 45
print('{}°F = {}°C'.format(t, fahrenheit2celsius(t)))
