# numbers = [1, 2, 3, 4, 5, 6, 7]
# for n in numbers:
#     print(n)

# numbers = (1, 2, 3, 4, 5, 6, 7)
# for n in numbers:
#     print(n)



# numbers = {1, 2, 3, 4, 5, 6, 7}
# for n in numbers:
#     print(n)

# user = {
#     'name': 'George',
#     'age': 25,
#     'skill': 'swim',
# }

# for key in user:
#     print()

# print('dict values')
# for val in user.values():
#     print(val)

# print('dict items ')
# for key, val in user.items():
#     print('key = ', key, 'val = ', val)

for val in [1, 2, 3, 4, 5, [3, 4, 6, 43], (3, 4, 34, 345)]:
    print(val)
    if isinstance(val, (list, set, tuple)):
        for i in val:
            print(i)

# val = ['12']
# if type(val) == int or type(val) == str:
#     print(True)
# else:
#     print(False)


# # с копированием 
# a = [2, 3, 4]
# b = a.copy()
# b.append(43)
# print('a=', a, 'b=', b)

# # с копированием 
# a = [2, 3, 4, [2, 3]]
# b = a.copy()
# b[2] = 400
# b[3][1] = 12
# print('a=', a, 'b=', b)

# # Модуль для глубокого копирования 
# import copy

# a = [2, 3, 4, [2, 3]]
# b = copy.deepcopy(a)
# b[2] = 400 
# b[3][1] = 12
# print('a =', a, 'b =', b)

a = 'csordaew'
if type(a) == str:
    print(a[::-1][::2])