'''
Можете прочитать
    Complex
    Decimal
    Fraction

Изменяемые
    set - множество
    dict - словарь
    list - список

Неизменяемые
    bin
    tuple - кортежи
    frozenset - множество
    int  
    float
    bool
    None
'''
names = [1, 2, 3, 4, 5, 6, 23.5, 'aaa', True, None]
names[0] = True
print(names)
names = list() # []

names = [[3, 4, 5], [3, 4, 5, 6], ['go', 'go1', 'go2']] # вывести на экран 'go2'
print(names[2][2])


# Нарезка - Slices
# интерировать - проходиться по элементам интерируемых переменных (эти такие переменные, которые могуть хранить больше одного значения) 
numbers = [2, 4, 54, 6, 454, 645]

print(numbers[1:5]) # 5 индекс не включительно
print(numbers[:], numbers)
print(numbers[1:])
print(numbers[:5])

print(numbers[:6:2])
print(numbers[:6])
print(numbers[::2])
print(numbers[::10])

print(numbers[-1])