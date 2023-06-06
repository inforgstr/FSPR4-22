# Используя исключения, исправьте код ниже
staff = {
    "Austin": {"floor managers": 1, "sales associates": 5},
    "Melbourne": {"floor managers": 0, "sales associates": 8},
    "Beijing": {"floor managers": 2, "sales associates": 5},
}


def print_staff_report(location, staff_dict):
    try:
        managers = staff_dict["floor managers"]
        sales_people = staff_dict["sales associates"]
        ratio = sales_people / managers
    except (KeyError, ZeroDivisionError) as error:
        return error
    print("Instrument World " + location + " has:")
    print(str(sales_people) + " sales employees")
    print(str(managers) + " floor managers")
    print("The ratio of sales people to managers is " + str(ratio))


for location, staff in staff.items():
    # Write your code below:
    print_staff_report(location, staff)

# Создайте собственное исключение и выведите её во время возникновения ошибки
inventory = {"Piano": 3, "Lute": 1, "Sitar": 2}

# Write your code below


class ItemNotInSeq(Exception):
    def __init__(self, supply, *args: object):
        super().__init__(args)
        self.supply = supply

    def __str__(self):
        return "We don't " + str(self.supply) + " in stock!"


def submit_order(instrument, quantity):
    if instrument not in inventory:
        raise ItemNotInSeq(instrument)
    supply = inventory[instrument]
    # Write your code below
    inventory[instrument] -= quantity
    print("Successfully placed order! Remaining supply: " + str(supply))


instrument = "Piano"
quantity = 5

try:
    submit_order(instrument, quantity)
except ItemNotInSeq as error:
    print(error)

# Также к задаче выше, добавьте возможность ошибке вернуть сообщение ошибки: 'We don't' + str(self.supply) + ' in stock'
