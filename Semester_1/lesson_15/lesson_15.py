'''
LEGB - Local Enclosed Global Built-in
       Локальный Вложенный Глобальный Встроенный
'''
# print(print)

# name = 'Behruz' # Global

# def get_name():
#     name = 'George' #  Local
#     print(name)

# get_name()

# # Modifying Global variables
# name = 'Dave'
# def spam():
#     global name
#     name = 'Guido'

# spam()
# # code
# print(name) # Dave


# def foo(items):
#     items.append(42)

# a = [1, 2, 3]
# foo(a)
# print(a)

# # VS
# def bar(items):
#     items = [4, 5, 6]

# b = [1, 2, 3]
# bar(b)
# print('b не поменялось', b)

# a = [1, 2, 3]
# b = a 
# b = [2, 4]
# b.append(43)
# print(a, b)


# a = 1
# def parent():
#     a = 5
#     def answer():
#         return a
#     return answer()

# print(parent())


# Local Enclosed Global Builtin
# GLobal
# a = 20
# def parent():
#     a = 5
#     def answer():
#         # local
#         a = 10
#         def get():
#             return a
#         return get()
#     return answer()

# print(parent())


# def outer():
#     # enclosed
#     x = 'local'
#     def inner():
#         # local
#         nonlocal x 
#         x = 'non local'
#         print('inner:', x)
#     inner()
#     print('outer:', x)

# outer()


# def factorial(n):
#     for i in range(1, n):
#         f = n * i
#         n = f
#     return f

# print(factorial(8))

# f = 'names'
# print(f.split())