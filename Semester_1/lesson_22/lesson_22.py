'''
ООП - Объектно Ориентированное програмирование
'''
# CamelCase
# snakeCase




class Marker:
    size = 10
    health = 10
    # функции - методами
    def __init__(self, company, color, price):
        # переменные - атрибутами
        self.company = company
        self.color = color
        self.price = price

    # classes' method
    def draw(self, line_length):
        if self.health <= 0:
            return 'Маркер истощён 0'
        if line_length > self.health:
            return f'Нарисовал {self.health} раз, осталось {abs(self.health - line_length)} раз'
        self.health -= line_length

marker = Marker('Marker Inc.', 'red', 34)
marker2 = Marker('Mark Inc.', 'blue', 23)
marker3 = Marker('Mark Inc.', 'blue', 36)
# obj = {} # копию - экземпляр объекта function

print(marker.draw(15))


# print(dir(marker))
# print(marker.company, marker.price, 
#     marker.color, marker.size)

# print(marker2.company, marker2.price, 
#     marker2.color, marker2.size)
