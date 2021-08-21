class Student:
    pass

class Marks:
    pass

student = Student()
marks = Marks()

print(isinstance(student, Student))
print(isinstance(marks, Marks))
print(issubclass(Student, object))
print(issubclass(Marks, object))
