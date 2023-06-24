"""
Контрольная работа 2 Семестр

Вопросы
    Теория
    1. Что такое генератор и какие виды генератора существуют? Приведите примеры
    2. Опишите цикл работы протокола итератора
    3. Можно ли создать итератор из итератора? Если да, то как?
    4. У нас есть программа, в который написаны функции для pvp игры с функцией attack, 
    
    которая возвращает урон от удара и принимает аргументы: damage, shield и health. 

    Разработчикам нужно изменить эту функцию, чтобы она учитывала эффект усиления защиты. 

    Как вы думаете, эффект защиты должен быть добавлен к shield внутри этой функции или вне?

    5. Для чего нужен .pyc файл и что это такое?
"""
"""
Теория
1. Генератор это функция возвращающая итератор в ответе, 
и при каждой итерации (вызов метода __next__) 
происходит переход к последующим значениям.
Генератор ведет себя как итератор.

Генераторы бывают двух типов:
- генераотор выражение (generator expression)
    - который возвращает генератор, пример:
"""
some_generator = (x for x in range(10))

"""
- И генератор функция который работает точно как итератор
и обеспечивает более быстрый и простой способ создания итераторов
"""


def generator_function():
    for i in range(10):
        yield i


"""
2.
Цикл работы протокола итератора

При цикле вызов метода next() происходит до тех пор пока не выдаст ошибку StopIteration.
Но можно и определять и настраивать поведение перебора при создании custom class.


3.
Да можно. Так как итератор можно получить из итерируемых объектов. 
Это те объекты у которых можно исчеслять элементы.


4. 
Вне функции, как я думаю каждая атака извлекает определенный health и при этом каждый раз делает при вызове функции .


5.

.pyc - Это скомпилированный выходной файл, созданный из исходного кода (при запуске исодного кода).
"""


# Задачи
"""
1. Создайте класс Staff, который описывает работника с атрибутами:
    name
    last_name
    photo - должно быть создано используя модуль Pillow
    position
    salary
    age
    department
Реализуйте 3 функции для работы с классом:
    1. Создает сотрудника (экземляр класса) и сохраняет его данные в csv файл staff.csv
    2. Функция для чтения файла staff.сsv, которая выводит список всех сотрудников
    3. Функция, которая возвращает список сотрудник фильтруя их по last_name и department
"""
# Решение


"""
2. Создать класс Load, который описывает груз c атрибутами:
    load_id
    qunatity 
    status - Not loaded/On the Way/Warehouse
    purchase_id
    wagon_id

Создать класс Wagon, который описывает вагон c атрибутами:
    wagon_id
    type - возможные значения: Wagon/Truck/Ship
    status
    shipping_date - должно быть датой 
    location 
    products 
    updated_at - должно быть датой
    created_at - должно быть датой

Создать класс Purchase, который описывает покупку c атрибутами:
    purchase_id
    product_name
    qunatity 
    price
    created_at - должно быть датой 
    uploaded_at - должно быть датой 

    4 метода:
        1. create_load(аргументы для создания груза) для создания экземпляра от класса Load 
        2. attach_wagon(аргументы для создания вагона) для создания экземпляра от класса Wagon
        3. ship_load() - должен вызывать методы create_load и attach_wagon и создаёть груз с вагоном
        4. list_of_loads() Выводит на экран список грузов с данными вагона, который перевозит этот груз 
"""
# Решение

"""
Задачи
1.
"""
import csv

from PIL import Image
from pathlib import Path


class Staff:
    def __init__(self, name, last_name, position, salary, age, department):
        img_path = Path(__file__).parent / "img" / f"{name}_{last_name}.png"
        # open image and save to self.profile_photo
        width = 500
        height = 400

        img = Image.new(mode="RGB", size=(width, height))
        img.save(img_path, format="png")

        self.name = name
        self.last_name = last_name
        self.position = position
        self.photo_path = img_path
        self.salary = salary
        self.age = age
        self.department = department


def add_data_csv(name, last_name, position, salary, age, department):
    path = Path(__file__).parent / "staff_csv.csv"

    try:
        with open(path, "r", newline="", encoding="utf-8") as file:
            reader = list(csv.DictReader(file))

            for row in reader:
                if name in row.values() and last_name in row.values():
                    return "Staff is already exists."
    except FileNotFoundError as error:
        return error

    staff = Staff(name, last_name, position, salary, age, department)
    photo_path = staff.photo_path

    try:
        with open(path, "a", newline="", encoding="utf-8") as csv_file:
            fields = [
                "Name",
                "Last_name",
                "photo_path",
                "position",
                "salary",
                "age",
                "department",
            ]
            writer = csv.DictWriter(
                csv_file,
                fieldnames=fields,
            )
            writer.writerow(
                {
                    "Name": name,
                    "Last_name": last_name,
                    "photo_path": photo_path,
                    "position": position,
                    "salary": salary,
                    "age": age,
                    "department": department,
                }
            )
    except FileNotFoundError as error:
        return error

    return fields


def get_list_staff():
    path = Path(__file__).parent / "staff_csv.csv"
    list_staff = []
    with open(path, "r", encoding="utf-8") as csv_file:
        for row in csv.DictReader(csv_file):
            list_staff.append(list(row.values()))

    return list_staff


def get_staff_by_filter():
    path = Path(__file__).parent / "staff_csv.csv"
    staff = []
    with open(path, "r", encoding="utf-8") as file:
        data = csv.DictReader(file)
        for row in data:
            staff.append(row)

    return sorted(staff, key=lambda x: x["Last_name"] and x["department"])


"""
2.
"""
from datetime import datetime


class Load:
    def __init__(self, load_id, quantity, status, purchase_id, wagon_id):
        if status.lower() not in ("not loaded", "on the way", "warehouse"):
            raise TypeError

        self.load_id = load_id
        self.qantity = quantity
        self.status = status
        self.puchase_id = purchase_id
        self.wagon_id = wagon_id


class Wagon:
    def __init__(
        self,
        wagon_id,
        type,
        status,
        shipping_date,
        location,
        products,
    ):
        if type.lower() not in ["truck", "ship", "wagon"]:
            raise TypeError

        self.wagon_id = wagon_id
        self.type = type
        self.status = status
        self.shipping_date = shipping_date
        self.location = location
        self.products = products
        self.updated_at = datetime.now()
        self.created_at = datetime.now()


"""
4 метода:
        1. create_load(аргументы для создания груза) для создания экземпляра от класса Load 
        2. attach_wagon(аргументы для создания вагона) для создания экземпляра от класса Wagon
        3. ship_load() - должен вызывать методы create_load и attach_wagon и создаёть груз с вагоном
        4. list_of_loads() Выводит на экран список грузов с данными вагона, который перевозит этот груз 
"""


class Purchase:
    def __init__(
        self, purchase_id, product_name, qunatity, price, created_at, uploaded_at
    ):
        self.purchase_id = purchase_id
        self.product_name = product_name
        self.quantity = qunatity
        self.price = price
        self.created_at = datetime.now()
        self.uploaded_at = datetime.now()
        self.loads = []

    def create_load(self, load_id, quantity, status, purchase_id, wagon_id):
        load = Load(load_id, quantity, status, purchase_id, wagon_id)
        return load

    def attach_wagon(self, wagon_id, type, status, shipping_date, location, products):
        wagon = Wagon(wagon_id, type, status, shipping_date, location, products)
        return wagon

    def ship_load(self, load_id, quantity, status, wagon_id, type, shipping_date, location, products):
        load = self.create_load(load_id, quantity, status, wagon_id)
        wagon = self.attach_wagon(wagon_id, type, status, shipping_date, location, products)
        self.loads.append(load, wagon)
        return load, wagon

    def list_of_loads(self, loads):
        for load in loads:
            load = load[0]
            print("Load id:", load.load_id)
            print("Quantity:", load.quantity)
            print("Status:", load.status)
            print("Purchase id:", load.purchase_id)
            print("Wagon ID:", load.wagon_id)


# 3. Переписать данную функцию, используя генератор функцию, выведите ответ от каждого выражения и напишите коментарий того, что происходит
def rewrite(numbers_1, numbers_2):
    a = set(numbers_1)
    b = set(numbers_2)

    # Возвращает множество, являющееся объединением множеств
    yield a | b

    # Возвращает множество, являющееся пересечением множеств
    yield a & b

    # Удаляет из множества a все элементы входящие в b
    yield a - b

    # Возвращает симметрическую разность множеств a и b (элементы, входящие в a или в b, но не в оба из них одновременно)
    yield a ^ b


# Решение

# 4. Напишите полный декоратор, который принимает аргумент slow_rate (int) и с помощью замедляет выполнение любой функции на это значение
# Решение
import time


def slow_decorator(slow_rate):
    def decorator(func):
        def wrapper(*args, **kwargs):
            try:
                time.sleep(slow_rate)
                return func(*args, **kwargs)
            except TypeError as error:
                return error

        return wrapper

    return decorator


# Example
# @slow_decorator(3)
# def add(a, b):
#     return a + b
# print(add(3, 4))


# 5. Используйте исключения и обходите возможные ошибки при работе с приведенныеми задачами выше
