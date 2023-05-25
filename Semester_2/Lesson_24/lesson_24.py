# class FishInventory:
#     def __init__(self, fishList) -> None:
#         self.available_fish = fishList

#     def __iter__(self):
#         self.index = 0
#         return self

#     def __next__(self):
#         if self.index < len(self.available_fish):
#             fish_status = self.available_fish[self.index]
#             self.index += 1
#             return fish_status
#         else:
#             raise StopIteration


# iterator = FishInventory([1, 2, 3, 4]).__iter__()
# for iter in iterator:
#     print(iter)


# class CustomerCounter:
#     def __init__(self, customer_list) -> None:
#         self.customer = customer_list

#     def __iter__(self):
#         self.index = 0
#         return self
    
#     def __next__(self):
#         if self.index > 100 or self.index == len(self.customer):
#             raise StopIteration
        
#         customer_queue = self.customer[self.index]
#         self.index += 1
#         return customer_queue


# iterator = CustomerCounter(list(range(110)))

# for iter in iterator:
#     print(iter)

"""Generators"""

def course_generator():
    """
    Creates generator with yield method
    """
    yield 'Computer Science'
    yield 'Art'
    yield 'Business'

courses = course_generator()
# for course in courses:
#     print(course)


# def func():
#     student_info = {
#         'Joan': 355,
#         'Billy': 300,
#         'Tory': 299,
#         'Kily': 100, 
#     }

#     for student in student_info:
#         name = student
#         id = student_info[name]
#         if not(id%3 and id%5):
#             yield student + ' gets prize C'
#         if not(id%3):
#             yield student + ' gets prize A'
#         if not(id%5):
#             yield student + ' gets prize B'

# prizes = func()
# for prize in prizes:
#     print(prize)

# def fib_generator(n):
#     fib = (x-2 + x-1 for x in range(1, n+1) if x > 1 )
#     return fib

# fibbonnaci = fib_generator(5)
# print(list(fibbonnaci))

# def student_standing_generator():
#     student_standing = ['Freshman', 'Senior', 'Junior', 'Freshman']
#     for student in student_standing:
#         if student == 'Freshman':
#             yield 500

# print(list(student_standing_generator()))


# def cs_generator():
#     for i in range(1, 5):
#         yield 'Computer Science ' + str(i)

# print(list(cs_generator()))
