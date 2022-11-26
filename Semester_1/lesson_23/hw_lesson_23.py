class Student:
    grades = []
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
    
    def add_grade(self, grade):
        if self.grades == []:
            self.grades.append(grade)
        else:
            self.grades.pop(0)
            self.grades.append(grade)
    
    def get_average(self):
        return ((self.grades) / len(self.grades))

student = Student('F', 'sdf')
student_1 = Student('F', "sdf")
student.add_grade(78)
student_1.add_grade(67)
print(student.grades == [78])
print(student_1.grades == [67])