class Rectangle():
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def get_length(self):
        return self.length

    def get_width(self):
        return self.width

    def area(self):
        return self.length * self.width 

myRect = Rectangle(10, 5)
print('Surface du rectangle (L=%d, l=%d) : %d' % (myRect.get_length(), myRect.get_width(), myRect.area()))
