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

stu1 = Student(1, 'christof', 'ONE')
print(f"student: {getattr(stu1, 'id')} {getattr(stu1, 'sname')} {getattr(stu1, 'sclass')}") 
setattr(stu1, 'sname', 'christophe')
setattr(stu1, 'sclass', 'TWO')
print(f"student: {getattr(stu1, 'id')} {getattr(stu1, 'sname')} {getattr(stu1, 'sclass')}") 
