# Вопросы
# 1
# Виртуальная машина (часто сокращается до ВМ) мало чем отличается от физических компьютеров — ноутбука, смартфона или сервера. У нее есть ЦП, 
# память, диски для хранения файлов и возможность подключения к Интернету. Компоненты вашего компьютера (аппаратная часть) материальны и осязаемы, тогда как виртуальные машины часто рассматриваются как виртуальные или программно-определяемые компьютеры в физических серверах, существующие только в виде кода.

# 2 
'''Всего в питоне есть 4 базовых переменных - это - integer, float, string, boolean. Integer - это целые числа, 
float - вещественные то есть дробные числа, string - это обычная строка, float - это логические типы данных которые принимают либо True либо False.'''
# 3
'Immutable(неизменяемые) - это: int, str, float, bool, tuple. И mutable(изменяемые): list, set, dict.'
# 4
'''2 типов форматирования строк - это просто f'...{78}' и '.{0}..{1}'.format('name', 'age') '''

# 5 

'''is проверяет схожость id() типов переменных, а in проверяет есть ли переменная в другом типе переменного'''

# 6 
'''LEGB'''
'''То есть L - локальный, E - вложенный, G - глобальный, B - встроенный'''


# 7 
'''Она возвращает - None(тип переменных)'''




'''Задачи'''
# 1 ye
# def min_length(n):
#     res = []
#     for i in n:
#         res.append(len(i))
#     return min(res)
            


# print(min_length(['asdf', 'hgh', 'fd', 'sdfs;lhj']))
# def short_word(names):
#     if names:
#         length = len(names[0])
#     else:
#         return False
#     for name in names[1:]:
#         name_len = len()
#         if name_len < name:
#             length = name_len



# names = ['sfdas', 'afasda', 'asdfsdfsfff']
# print(result = short_word(names))

# -----------------------------------------------------------------------

# 2 no

# def number_to_words(n):
#     f = {1 : 'one', 2 : 'two', 3 : 'three', 4 : 'four', 5 : 'five',
#     6 : 'six', 7 : 'seven', 8 : 'eight', 9 : 'nine'}
#     l = {10 : 'ten', 20 : 'twenty', 30 : 'thirty', 40 : 'fouty',
#     50 : 'fifty', 60 : 'sixty', 70 : 'seventy',
#     80 : 'eighty', 90 : 'ninety'}
#     s = {11 : 'eleven', 12 : 'twelve', 13 : 'thirteen',
#     14 : 'fourteen', 15 : 'fivteen', 16 : 'sixteen',
#     17 : 'seventeen', 18 : 'eighteen', 19 : 'ninteen'}
#     n1 = n % 10
#     n2 = n - n1
#     if n < 10:
#         return f.get(n)
#     elif 20 > n > 10:
#         return s.get(n)
#     elif n >= 10 and n2 == 0:
#         return l.get(n)
#     elif n > 20:
#         return l.get(n2) + ' ' + f.get(n1)

# print(number_to_words(11))

# ------------------------------------------------------------------

# 3 ye
# string = "You've got that fire (fire). The flavor, the style (style)"
# print(string.split('.'))

# -------------------------------------------------------------------------

# 4 ye
# names = [] 
# for i in range(10): 
#     names.append(i + 4) 
#     if i == 7: 
#         names.pop(0) 

# print(names)
# ---------------------------------------------------------------
# 5 ye
# string = ['John', 'Hi', 'numbers', 'Code']
# if 'John' in string:
#     print('John')
# else:
#     print(-1)
# --------------------------------------------------------
# 6 ye
# dictionary = {'age': 45, 'race': 'sdf', 'l': 56}

# if 'age' in dictionary and 'race' in dictionary and isinstance(dictionary['age'], int):
#     print('age is', dictionary['age'], '\nrace is', dictionary['race'])

# else:
#     print('human')
