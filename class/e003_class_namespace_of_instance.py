class my_class:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def print(self):
        print('a=', self.a, 'b=', self.b)

obj = my_class(a=10, b='test')
print(obj.__dict__)

obj.print()
