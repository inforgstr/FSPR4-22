# 2 task
# Создать класс, который описывает машину с атрибутами: модель, цвет, цена, страна, двигатель ...
# и с методами: ускорение за секунду, расход топлива за прохожденный путь (если топливо закончится, 
# вывести на экран пройденный путь и оставшийся)

class Car:
    # 1л - 10 км
    Fuel_way = 300 # путь
    def __init__(self, model, color, price, country, engine):
        self.model = model
        self.color = color
        self.price = price
        self.country = country
        self.engine = engine
    def acceleration(self, acc): # ускорение
        return f'{acc} м/с - ускорение'
    def fuel(self, fl): # fl - топливо
        if fl < self.Fuel_way/10:
            return f'{fl*10} км пройденный путь \n{self.Fuel_way - fl*10} км оставшийся путь'
        elif fl > self.Fuel_way/10:
            return f'{fl*10} км пройденный путь\n'
    
car = Car('BMW', 'blue', '70000 $', 'Germany', 'N57D30S1')
print("Car's characteristic:", "\nModel:", car.model, "\nColor:", car.color, 
    "\nPrice:", car.price, '\nCountry:', car.country, 
    '\nEngine:', car.engine, '\n\n')
print(car.acceleration(12))
print(car.fuel(40))

# 3 task 
# Создать класс описывающий человека с методами которые описывают вас (что умеете)
class Human:
    def head(self):
        return 'Head can think'
    def legs(self):
        return 'Legs can run'
    def hands(self):
        return 'Hands can write'
human = Human()
print(human.head())
print(human.legs())
print(human.hands())