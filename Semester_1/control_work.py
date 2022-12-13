# Вопросы: 
# 1
'''
int, float, str, list, dict, tuple, set, frozenset, bool, None
int - не итерируемый, имеет неограниченную точность, может принимать сколь угодно большие значения(только целые числа).
str - итерируемый, строковый тип str в Python используют для работы c любыми текстовыми данными. Python автоматически определяет тип str по кавычкам - одинарным или двойным.
float - не итерируемый, имеет неограниченную точность, могут принимать сколь угодно большие значения и может округлять(дробные числа).
dict - c помощью словарей можно разрабатывать эффективные структуры данных;
    словари могут содержать объединенные данные в виде записей;
    словари эффективны при представлении разреженных структур данных.
list - можно непосредственно изменять c помощью операции присваивания.
tuple - Если есть данные, которые не изменяются, реализация их в виде кортежа гарантирует, что они остаются защищенными от изменений.
set - эффективен при операций c математическими вычислениями чем другие типы переменных.
bool -  не позволяет наследоваться. Его единственные экземпляры — False и True.
None - может служить как bool - False при логических условиях.
frozenset - Отличие здесь заключается в том, что элементы в frozenset нельзя изменить в дальнейшем. Можно сказать, что это смесь множества и кортежа.
'''

# 2
'''
В качестве ключа словарья и значением множества можно хранить любые типы переменных.
'''

# 3
'''
MRO - Описывает путь поиска класса, 
который используется для получения соответствующего метода в классах, содержащих наследование.

Наследование - способность передавать данные и методы одного класса другим классам.
'''

# 4
'''
Чтобы узнать нынешний статус проекта нужно ввести комманду - git status
Потом нужно добавить порект в локальную часть репозитория с помощью команды - git add .(для добавления всех изменённых файлов), git add <какой-то файл> (для добавления по одному)
И нужно ввести комманду - git commit -m "Коммит" - позволяет системе поэтапно сохранять изменения.
Последнее это - git push - чтобы опубликовать изменения проекта с данным коммитом. 
'''

# 5 
'''
В методе всегда используються объекты, а в функции объект не нужен. 
'''

# Теория + задачи
# 1
'''
Сравнения
==,  !=,   >=,   <=,  < ,  >

Логические
and, or, not, in, is, id, not in

Особые
&, ^, |
'''

# 2
'''
Полиморфизм - способность объекта принимать множества форм

Пример:
class Father:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
class Son(Father):
    pass
print(Son('John', 18).name)
'''

# 3 
'''
Было:
def validate(username, password):
    username "Random" password 2321ewfsef
    return "Вы успешно вошли в систему!"
    return Пароль или имя пользователя не правильны

Стало:
def validate(username, password):
    return "Вы успешно вошли в систему!" if username == 'Random' and password == '2321ewfsef' else 'Пароль или имя пользователя не правильны'
'''

# 4
'''
LEGB - Local Enclosed Global Built-in

age = 18 # Global
def greeting(name):
    print(name) # Local
    def f(age):
        return age # Enclosing
    print(f(23))

print() # Built-in
'''
# 5
'''
Рекурсия - это когда функция вызывает самого себя, то есть вызывает себя через ссылки.

def factorial(n):
    return 1 if n <= 1 else n*factorial(n-1)
'''

# Задачи
# 1
def get_data(code, salary, *args, **kwargs):
    other_info = []
    other_info.append(code)
    other_info.append(salary)

    for arg in args:
        other_info.append(arg)

    for key, val in kwargs.items():
        other_info.append((key, val))

    return other_info
print(get_data('876', 1293, (12, 213232, 421), d='sadf'))

# 2
'''Создать класс Gum, который описывает жевачку с 
атрибутами: smell, price, company, name, special_features, count и с методом str, который возвращает информацию о жевачке со всеми атрибутами. 
От класса Gum создать два других класса: Orbit и Trident. Orbit должен иметь ещё один атрибут country (страна произвдства). 
Trident должен иметь ещё один атрибут date_of_production (дата производства).
'''
class Gum:
    def __init__(self, smell, price, company, name, special_features, count):
        self.smell = smell
        self.price = price
        self.company = company
        self.name = name
        self.special_features = special_features
        self.count = count
    def __str__(self):
        return f'taste - {self.smell}\nprice - {self.price}\ncompany -  {self.company}\nname - {self.name}\nspecial_features - {self.special_features}\ncount - {self.count}'

class Orbit(Gum):
    def __init__(self, smell, price, company, name, special_features, count, country):
        super().__init__(smell, price, company, name, special_features, count)
        self.country = country

class Trident(Gum):
    def __init__(self, smell, price, company, name, special_features, count, date_of_production):
        super().__init__(smell, price, company, name, special_features, count)
        self.date_of_production = date_of_production
    
orbit = Orbit('324', 2342, 3245, 3453, 345, 345, 34)
print(orbit.country)
trident = Trident('324', 2342, 3245, 3453, 345, 345, 34)
print(trident.date_of_production)



# 3 
def is_defended(attackers, defenders):
    surviving_attackers = 0
    surviving_defenders = 0

    if len(attackers) != len(defenders):
        dop = [i * 0 for i in range(len(attackers) - len(defenders))]
        if len(attackers) > len(defenders):
            defenders += dop
        else:
            attackers += dop

    d = []
    for i in range(len(defenders)):
        d.append([defenders[i], attackers[i]])

    for pair in d:
        if pair[0] - pair[1] > 0:
            surviving_defenders += 1
        elif pair[0] - pair[1] < 0:
            surviving_attackers += 1

        
    if surviving_defenders > surviving_attackers:
        return True
    elif surviving_defenders < surviving_attackers:
        return False
    else:
        return True if sum(defenders)>= sum(attackers) else False