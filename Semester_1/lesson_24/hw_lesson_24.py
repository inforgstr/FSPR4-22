#  Создать класс с методами для умножения, возведения в степень, нахождения площади квадрата, круга и треугольника 
from math import*
class Functions:
    def area_rectangle(self, a, b):
        return a * b
    def area_circle(self, radius):
        return (radius**2) * pi
    def area_triangle(self, a, b, c):
        p = (a+b+c)/2
        ar = int((p*(p-a)*(p-b)*(p-c))**1/2)
        return ar
    def power(self, a, terms):
        return a**terms
    def multiply(self, a, b):
        return a * b
func = Functions()
print(func.area_rectangle(208, 56), func.area_triangle(4, 5, 6))
print(func.power(45, 7), func.multiply(78, 45))

# 2. Создать класс, который описывает игрового персонажа с атрибутами (health, mana, damage, type, skill) и методами attack, heal, level_up 
# от которого наследуются 3 класса Archer, Paladin, Wizard. На свою фантазию можете расширить функциональность 
class Player:
    def __init__(self, health, mana, damage, type, skill):
        self.health = health
        self.mana = mana
        self.damage = damage
        self.type = type
        self.skill = skill
    def attack(self):
        return self.damage
    def heal(self):
        return self.health
    def level_up(self):
        if 20 < self.health and self.mana > 20 and self.damage > 20:
            return 'LEVEL UP!'

class Archer(Player):
    pass
class Paladin(Player):
    pass
class Wizard(Player):
    pass
player = Paladin(34, 23, 345, 'afd', 'yo')
player1 = Archer(40, 76, 50, 'af', 'high')
print('Атака персонажа(Archer)', player1.attack())
print(f'Здоровье персонажа(Paladin) {player.heal()}')

# 3. Из кодварса решить две (хотя бы одну) по ссылку по ООП:

# 1)Building blocks    -   Link: https://www.codewars.com/kata/55b75fcf67e558d3750000a3
class Block:
    def __init__(self, n):
        self.n = n
    def get_width(self):
        return self.n[0]
    def get_length(self):
        return self.n[1]
    def get_height(self):
        return self.n[2]
    def get_volume(self):
        s = 1
        for i in self.n:
            s *= i
        return s
    def get_surface_area(self):
        return (self.n[0]*self.n[1]+self.n[0]*self.n[2]+self.n[1]*self.n[2])*2

block = Block([23, 45, 34])
print('Площадь поверхности призмы -', block.get_surface_area())

# 2)Refactored Greeting    -   link: https://www.codewars.com/kata/5121303128ef4b495f000001/train/python
class Person:
    def __init__(self, n):
        self.name = n
    def greet(self, names):
        return f'Hello {names}, my name is {self.name}'

person = Person('Joe')
print(person.name)
print(person.greet('Kate'))