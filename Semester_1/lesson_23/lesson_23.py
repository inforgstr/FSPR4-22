'''
Overloading - перезаписывание логики метода на 
'''
class PlayerCharacter:
    def __init__(self, hobby, name='anonymous', age=0):
        self.name = name
        self.age = age
        self._hobby = hobby

    def _welcome(self):
        return "Hi!"

    def shout(self):
        return f'{self._welcome()} My name is {self.name} and my hobby is {self._hobby}.'

    @classmethod
    def adding_things_2(cls, num1, num2):
        # PlayerCharacter(num1+num2)
        return cls(num1+num2)
    
    @classmethod
    def adding(cls, a, num1, num2):
        return cls(a, num1*num2)

    @staticmethod
    def multiply(a, b): # не принимает self
        return a * b


player_1 = PlayerCharacter('Jerry', 20)
print(player_1.shout())
# print(player_1.multiply(34, 4543))
# player2 = PlayerCharacter(0, 34)
# print(player2.name, player2.age)


# player_2 = PlayerCharacter.adding_things_2(2, 20)
# print(player_2.age, player_2.name)
# player_3 = PlayerCharacter.adding('KLJ', 23, 3)
# print(player_3.age, player_3.name)

