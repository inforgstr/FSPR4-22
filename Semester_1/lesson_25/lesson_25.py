# class BaseCharacter:
#     experience = 0
#     lvl = 1

#     def __init__(self, health, mana, damage, type, skills):
#         self.health = health
#         self.mana  = mana
#         self.damage = damage
#         self.type = type
#         self.skills = skills

#     def attack(self, enemy_health):
#         return enemy_health - self.damage
    
#     def heal(self):
#         if 'heal' in self.skills:
#             self.health += 10

#     def enemy_killed(self, enemy_lvl):
#         if enemy_lvl == 1:
#             self.experience += 5
#             self.level_up()
#             print(f'You leveled up! Current level is {self.lvl}')
#     def level_up(self):
#         if 10 <= self.experience <= 20:
#             self.lvl += 1
#         elif 21 <= self.experience <= 30:
#             self.lvl += 1
#         elif 31 <= self.experience <= 40:
#             self.lvl += 1
#         elif 41 <= self.experience <= 50:
#             self.lvl += 1
#         elif 51 <= self.experience:
#             self.lvl += 1
# class Archer(BaseCharacter):
#     pass
# class Paladin(BaseCharacter):
#     pass
# class Wizard(BaseCharacter):
#     pass
# person = BaseCharacter(15, 20, 15, 'base', ['heal'])
# person_2 = BaseCharacter(15, 20, 15, 'base', ['heal'])
# print(person.attack(person_2.health))
# print(person_2.health)


# type(1)
# repr(1)

# __str__
# __repr__
class Person:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    # def __str__(self):
    #     return f"Class info: name {self.name} age = {self.age}"

    # def __repr__(self):
    #     return f"Class info: name {self.name} age = {self.age}"
    
    def __sub__(self, other):
        x = self.x - other.x
        y = self.y - other.y
        return Person(x, y)

person = Person(234, 23)
person_2 = Person(154, 18)
result = person - person_2
print(result.x, result.y)