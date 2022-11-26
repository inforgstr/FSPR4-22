# class Student:
#     grades = []
#     def __init__(self, first_name, last_name, grade=[]):
#         self.first_name = first_name
#         self.last_name = last_name
#         self.grades = list(grade)
    
#     def add_grade(self, grade):
#         self.grades.append(grade)
    
#     def get_average(self):
#         return sum(self.grades) / len(self.grades)

# johnDoe = Student('John', 'Doe')
# janeDoe = Student('John', 'Doe')
# jamesSmith = Student('James', 'Smith') 
# jennaSmith = Student('Jenna', 'Smith') 
# students = (johnDoe, janeDoe, jamesSmith, jennaSmith) # tuple 
 
# johnDoe = Student('John', 'Doe') 
# janeDoe = Student('Jane', 'Doe') 
# jamesSmith = Student('James', 'Smith') 
# jennaSmith = Student('Jenna', 'Smith') 
# students = johnDoe, janeDoe, jamesSmith, jennaSmith 
 
# firstAssessmentGrades = [63, 92, 82, 75] 
# for i, student in enumerate(students): 
#     student.add_grade(firstAssessmentGrades[i]) 
 
# for i, student in enumerate(students): 
#     print(student.grades[0], firstAssessmentGrades[i])


from datetime import*
class Father:
    import datetime
    house = True
    def __init__(self, name, job, hobby, bank_account):
        self.name = name
        self.job = job 
        self.hobby = hobby
        self.bank_account = bank_account

    def cook(self, products):
        if "carrot" in products and 'meat' in products and 'rice' in products:
            self.cooked_food = 'plov'
        else:
            print("We can't cook these products.")

    def date_of_birthday(self, year, month, day):
        import datetime
        return datetime.datetime(year, month, day)

    def spend(self, amount):
        self.bank_account -= amount
    def income(self, amount):
        self.bank_account += amount

class Mother:
    def cook(self, products):
        if "carrot" in products and 'meat' in products and 'rice' in products:
            self.cooked_food = 'plov'
        else:
            print("We can't cook these products.")

class Child(Father, Mother):
    def __init__(self, name, job, hobby, bank_account, age):
        super().__init__(name, job, hobby, bank_account)
        self.age = age
    def cook(self, products):
        super().cook(self, products)
        if 'oil' in products and 'баклажан' in products and 'помидор' in products:
            self.cooked_food = 'жаренный баклажан'


child = Child('Behruz', "IT", 'hiking', 19999, 19)
print(child.date_of_birthday(2005, 10, 7))
# print(child.birthday(234))
print(child.age)
# print(child.bank_account, child.house)
# child.spend(299)
# print(child.bank_account)
# child.income(2999)
# print(child.bank_account)
# c = C('sdf', 'IT', 'hiking', 33455)
# c.spend(355)
# print(c.bank_account)
# c.income(344444)
# print(c.bank_account)
