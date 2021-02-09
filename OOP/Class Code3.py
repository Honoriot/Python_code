
class Student:
    College = "Delhi Institute Of Tool Engneering"
    branch = ["Mechatronics", "Tool", "Mechanical"]
    def __init__(self, m1, m2, m3):
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3
        self.sub = self.subject()

    def avg(self):
        return (self.m1 + self.m2 + self.m3)/3

    @classmethod       # decorator
    def info(cls):
        return cls.College    

    @staticmethod
    def get_branch():
        return "This a college for all"

    class subject:
        def __init__(self):
            self.course = "mechatronic"
            if self.course == "mechatronic":
                self.num_subject = 40
            else:
                self.num_subject = 35


stu1 = Student(45, 78, 38)
print(stu1.info())
print(Student.info())
print(stu1.get_branch())
print(stu1.sub.num_subject)
stu1.sub.course = "tool"
print(stu1.sub.course)
stu1.sub.num_subject
print(stu1.sub.num_subject)

Sub1 = Student.subject()
print(Sub1.course)