# if 1==1:
#     print(True)

# def greet():
#     print("Hello")

# # вызов функции
# print(greet())

# def greet():
#     return "Hello"

# result = greet()
# print(result)

# def greet(name):
#     print(f'Hello {name}')
# greet('Bekhruz')
# s = 'Bekzod'
# greet(s)
# greet(input()) 

# def greet(name):
#     return f'Hello {name}'

# print(greet('Jamshid'))
# result = greet('Aybek')
# print(result)

def rectangle(length, width):
    star = '*'
    i = 0
    while i < length:
        if i > 0 and i < (length - 1): 
            empty = ' ' * (width - 2)
            print(f'{star}{empty}{star}')
        else:
            print(star * width)
        i += 1
l = int(input('Введите длину прямоугольника: '))
w = int(input('Введите ширину прямоугольника: '))
rectangle(l, w)


# def far_to_cel(far):
#     result = []
#     for f in far:
#         cel = (f - 32) * 5/9
#         result.append(cel)
#     return result
# r = [30, 20, 19, 24, 45]
# print(far_to_cel(r))

