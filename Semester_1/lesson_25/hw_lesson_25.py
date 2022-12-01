# 1. Перегрузить (написать свою) реализацию трех магических методов sub, mull, eq
class Person:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
    
    def __sub__(self, other):
        x = self.x - other.x
        y = self.y - other.y
        return Person(x, y)
    def __mull__(self, other):
        x = self.x * other.x
        y = self.y * other.y
        return Person(x, y)
    def __eq__(self, other):
        x = self.x == other.x
        y = self.y == other.y
        return Person(x, y)
    def __ge__(self, other):
        x = self.x >= other.x
        y = self.y >= other.y
        return Person(x, y)

person = Person(230, 344)
person_1 = Person(23, 34)
result = person == person_1
result_1 = person <= person_1
print(result.x, result.y)
print(result_1.x, result_1.y)