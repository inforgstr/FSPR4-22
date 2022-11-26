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
