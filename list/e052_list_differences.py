color1 = ["red", "orange", "green", "blue", "white"]
color2 = ["black", "yellow", "green", "blue"]

print('listes {} {}'.format(color1, color2))
print('color1 - color2 = {}'.format(list(set(color1).difference(color2))))
print('color2 - color1 = {}'.format(list(set(color2).difference(color1))))

# web solution
from collections import Counter
counter1 = Counter(color1)
counter2 = Counter(color2)
print("Color1-Color2: ",list(counter1 - counter2))
print("Color2-Color1: ",list(counter2 - counter1))
