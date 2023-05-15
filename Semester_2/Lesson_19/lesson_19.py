# # Global variable
# name = "John"

# def greet():
#     # Local variable
#     name = "Emma"
#     print(name)

# greet()
# print(name)


# # Enclosed
# name = "Emma"

# def greet():
#     name = "John"
#     def greeting():
#         nonlocal name
#         print(name)
#     greeting()

# greet()
# print(name)


# # Built-in
# from math import pi

# def inp():
#     def out():
#         print(pi)
#     out()

# inp()


# # 5 kyu - 1; 6 kyu - 2


# # dict
# a = {x:x+1 for x in range(1, 11)}
# print(a)

# # set
# a = {x for x in range(1, 11)}
# print(a)

# # list
# a = [x for x in range(1, 11)]
# print(a)


# answer = list(map(lambda x: x**2, [2, 3, 4, 5, 6, 7]))

# print(answer)


var = [2, [2 , 3, [[[[[[[[5]]]]]]]]]]

# sum = 0

# With for loop
# for i in range(10):
#     print("list:", var)
#     print("i:", i)
#     i = len(var)-1
#     if isinstance(var[i], list):
#         var = var[i]
#         print(var)
#         sum += 1

# print(sum)

# Recursive
# def wrapper(x):
    
#     if len(x) < 1:
#         return x
#     else:
#         wrapper(len(x)-1)

# wrapper(var)
