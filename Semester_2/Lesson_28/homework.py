import re


# Дз
# 1. Используя исключения, исправьте код ниже
staff = {
    "Austin": {"floor managers": 1, "sales associates": 5},
    "Melbourne": {"floor managers": 0, "sales associates": 8},
    "Beijing": {"floor managers": 2, "sales associates": 5},
}


def print_staff_report(location, staff_dict):
    managers = staff_dict["floor managers"]
    sales_people = staff_dict["sales associates"]
    ratio = sales_people / managers
    print("Instrument World " + location + " has:")
    print(str(sales_people) + " sales employees")
    print(str(managers) + " floor managers")
    print("The ratio of sales people to managers is " + str(ratio))


# for location, staff in staff.items():
#     try:
#         print_staff_report(location, staff)
#     except (KeyError, ZeroDivisionError) as error:
#         raise error

# 2. Используя исключения, исправьте код ниже и создайте собственное исключение,
# которое должно вывести ошибку, если количество покупаемых больше количеств товаров в наличии.
# Также добавьте сообщение для созданного исключения с строкой: 'We don't' + str(self.supply) + ' in stock'
inventory = {"Piano": 3, "Lute": 1, "Sitar": 2}


# Write your code below
class SupplyNotAvailable(Exception):
    def __init__(self, supply):
        self.supply = supply

    def __str__(self) -> str:
        return f"We don't " + str(self.supply) + " in stock"


def submit_order(instrument, quantity):
    supply = inventory[instrument]
    # Write your code below
    if supply < quantity:
        raise SupplyNotAvailable(instrument)

    inventory[instrument] -= quantity
    print("Successfully placed order! Remaining supply: " + str(supply))


instrument = "Guitar"
quantity = 5

# try:
#     submit_order(instrument, quantity)
# except (KeyError, SupplyNotAvailable) as error:
#     raise error

# 3. Написать регулярное выражения, для нахождения навыков программирования из данного списка слов
titles = [
    "Middle JavaScript Developer",
    "Middle JavaScript Developer (AngularJS 9)",
    "Middle JavaScript Developer (React)",
    "Senior JavaScript Developer (Angular)",
    "middle JavaScript angularjs node js",
]

for title in titles:
    patterns = r"([Jj]ava[Ss]cript|[Aa]ngular[Jj][sS]|[rR]eact|[Nn]ode[. ][jJ][sS])"

    found_string = ", ".join(re.compile(patterns).findall(title))
    print(f"Found: {found_string}")

# Навыки которые мы должны найти: javascript, angularjs, react, node js, node.js, nodejs
# При этом регистр не имеет значения, то есть angularjs и Angularjs - должно рассматриваться одинаково
