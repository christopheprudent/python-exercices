class Student:
    """
    define a student class w/ 3 attributs
    id
    name
    class
    """
    def __init__(self, id, sname, sclass):
        self.id = id
        self.sname = sname
        self.sclass = sclass

print(type(Student))
print(Student.__dict__.keys())
print(Student.__module__)
print(Student.__doc__)

stu1 = Student(1, 'christophe', 'BCAA')
print(type(stu1))
