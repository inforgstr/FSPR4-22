import re

# Используя исключения, исправьте код ниже
# staff = {
#     "Austin": {"floor managers": 1, "sales associates": 5},
#     "Melbourne": {"floor managers": 0, "sales associates": 8},
#     "Beijing": {"floor managers": 2, "sales associates": 5},
# }


# def print_staff_report(location, staff_dict):
#     try:
#         managers = staff_dict["floor managers"]
#         sales_people = staff_dict["sales associates"]
#         ratio = sales_people / managers
#     except (KeyError, ZeroDivisionError) as error:
#         return error
#     print("Instrument World " + location + " has:")
#     print(str(sales_people) + " sales employees")
#     print(str(managers) + " floor managers")
#     print("The ratio of sales people to managers is " + str(ratio))


# for location, staff in staff.items():
#     # Write your code below:
#     print_staff_report(location, staff)

# # Создайте собственное исключение и выведите её во время возникновения ошибки
# inventory = {"Piano": 3, "Lute": 1, "Sitar": 2}

# Write your code below


# class ItemNotInSeq(Exception):
#     def __init__(self, supply):
#         self.supply = supply

#     def __str__(self):
#         return "We don't " + str(self.supply) + " in stock!"


# def submit_order(instrument, quantity):
#     supply = inventory[instrument]

#     if instrument not in inventory:
#         raise ItemNotInSeq(instrument)
    
#     # Write your code below
#     inventory[instrument] -= quantity
#     print("Successfully placed order! Remaining supply: " + str(supply))


# instrument = "Piano"
# quantity = 5

# try:
#     submit_order(instrument, quantity)
# except KeyError as error:
#     print(error)

# Также к задаче выше, добавьте возможность ошибке вернуть сообщение ошибки: 'We don't' + str(self.supply) + ' in stock'

# pattern = re.compile("for")
# result = pattern.math("for")
# print(result)


# pattern = re.compile('for')


# full = re.compile("Look for the specific word for if you can.")
# string = "Look for the specific word for if you can."


# Scan through string looking for a match to the pattern,
# returning a Match object, or None if no match was


# a = re.search('specific', string)
# print(re.search('specific', string))
# print("group", a.group())
# print(a.span())
# print(a.start())
# print(a.end())


# a = pattern.search(string)
# print(a)

# b = pattern.findall(string)
# print(b)

# c = pattern.fullmatch(string)
# print(c)
