numbers = [1, 2, 3, 4, 5, 6 , 7]
print(numbers.append('Hello'))

numbers.extend([2, 3, 4, 45])
print(numbers)

numbers.pop()
print(numbers)
numbers.remove('Hello')
print(numbers)

words = ['foo', 'aga', 'aga', 'tall']
n = numbers.count(4)
print(n)

# ----------------------------------------------------------------------------
# Tuple - кортеж
numbers = (2, 3, 4, 5, 6)
print(numbers, numbers[3])
numbers = ((4,5), 4.5, 'fafa', [5, 6, 7])
print(numbers, numbers[3][0])

# numbers[1] = 'Changed'
# Список - изменяемый тип перменных 
# Кортежей можно Читать, Создавать
numbers = (2, 3, 4, [4, 5])
# numbers[3][0] = 24
print(numbers[3], numbers[3][0])

# 4 способа создать кортежи
numbers = (2, 3, 4, 5)
print('1', type(numbers), numbers)
numbers = tuple()
print(type(numbers), numbers)
numbers = ()
print(type(numbers), numbers)
numbers = 5, 4, 3, 2
print('Last', type(numbers), numbers)


a = [2, 3, 4]
a = tuple(a)
print(type(a))
a = tuple('Hello')
print(type(a), a)


# -------------------------------------------------------------------------------

# Матрица 
[2, 3, 4, 5, 6] # вектор 
matrix = [[2, 3, 4], [5, 6, 7]] # Матрица 3 столбца и 2 строки 
print( matrix[1][1] ) # 0 1 | 11 |
# 2  3  4
# 5  6  7
# random = list(1) # error
# random = list(True) # error

random = list('Random !@*(&&(*&^') 
splitted_string = 'Split me ! random'.split('me !') # ' ' 
print(random, splitted_string,''.join(random), sep='\n')


