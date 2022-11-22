# 2 task
# Создать класс, который описывает машину с атрибутами: модель, цвет, цена, страна, двигатель ...
# и с методами: ускорение за секунду, расход топлива за прохожденный путь (если топливо закончится, 
# вывести на экран пройденный путь и оставшийся)

class Car:
    # 1л - 10 км
    Fuel_way = 300
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
            return f'{fl*10} км пройденный путь'
    
car = Car('BMW', 'blue', '70000 $', 'Germany', 'N57D30S1')
print("Car's characteristic:", "\nModel:", car.model, "\nColor:", car.color, 
    "\nPrice:", car.price, '\nCountry:', car.country, 
    '\nEngine:', car.engine, '\n\n')
print(car.acceleration(12))
print(car.fuel(40))