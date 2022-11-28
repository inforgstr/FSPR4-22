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

