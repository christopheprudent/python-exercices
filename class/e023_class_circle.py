import math

class Circle():
    
    def __init__(self, radius):
        self.radius = radius

    def get_radius(self):
        return self.radius

    def area(self):
        return math.pi * (self.radius ** 2)

    def perimeter(self):
        return 2 * math.pi * self.radius

myCircle = Circle(1)
print('     Aire cercle de rayon r=%d : %f' % (myCircle.get_radius(), myCircle.area()))
print('Périmètre cercle de rayon r=%d : %f' % (myCircle.get_radius(), myCircle.perimeter()))
