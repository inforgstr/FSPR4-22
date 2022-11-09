print( 'in =', 1 in [2, 3, 4, 1] )
print('in =', 'Hi', 'Hi my name is SMTH')
print('in = ', [1, 2] in [2, 3, 4, [1, 2]])
print('in = ', {1, 2} in [2, 3, 4, {1, 2}])


if 1:
    print(True)
else:
    print(False)

if 0: # False
    print(True)
elif 2 == 2:
    print('elif 1')
elif 2 == 2:
    print('elif 1')
else:
    print(False)




# isinstance
name = 12
print(isinstance(name, (str, int)))


# is and ==
# == - сравнивает значения
# is - сравнивает id двух значений 
# id()
a = 1 
b = 1 
print(id(a), id(b))


t_2 = ()
t_1 = ()
# print(id(t_2), id(t_1))
print(t_1 == t_2)
print('tuple', t_1 is t_2 ) # True
# print('1 == 1', 1 == 1, 1 is 1)

l_1 = [1, 2]
l_2 = [1, 2]
print(l_1 == l_2)
print(l_1 is l_2) # False

d_1 = {1: 1}
d_2 = {1: 1}

print('dict', d_1 == d_2)
print('dict', d_1 is d_2) # False       


# print(l_1, id(l_1), l_2, id(l_2))

name = "Behruz"
skill = "D2"
age = 20
surname = 'Saidjonov'

# if name == "Sardor" and skill == 'D2': # And - и
#     print(name, skill)
# else:
#     print("AND")

# if name == "Sardor" or skill == 'D2': # Or - или
#     print(name, skill)
# else:
#     print("OR")

# # not - не
# if not age: # not -> False - True
#     print(age)
# else:
#     print("Age is False")
# # -----------------------------------------------------------------

# if (name == 'Behruz' and age > 18) or skill == 'D2':
#     print(name, age, skill)
# else:
#     print("invalid name, age, skill")


# if name == "Behruz" or age > 22 and skill == 'D2':
#     print(name, age, skill, 'second output')
# else:
#     print("Invalid name, age, skill")

# ----------------------------------------------------------------
# bool
# True | False
# любое число что не ноль - это правда 
# если переменная пустая - то она  ложь 

# True=1 False=0

# print(False * 3)
x = 10
y = 20 
if x>y:
    print(True)
else:
    print(False)

"name surname".split() # ['name', 'surname']
# a if condition else b
print( True if x > y else False )

# ==, !=, >, >=, <, <=, is, is not, in, not in, notm and, or
# [] {} () "" 0 - False
# 
if []: # False
    print(False)
if -19: # True
    print(True)
# ----------------------------------------------------------------------


