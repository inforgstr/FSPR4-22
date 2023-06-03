import csv
import time


"""
Functions for class Store
"""


def get_headers(file_path, delimiter=";"):
    with open(file_path, "r", encoding="utf-8") as headers:
        headers = csv.DictReader(headers, delimiter=delimiter).fieldnames

    return headers


def get_csvdata(file_path, delimiter=";"):
    with open(file_path, "r", encoding="utf-8") as data:
        data = csv.DictReader(data, delimiter=delimiter)

        for row in data:
            yield row


def update_csv(path, index, column, new_value, action, fieldnames, count=1):
    """
    Args:
        path(str): file path
        index(int): the index where should be changed
        column: column where should be changed
        new_value: new value that should be set up for exists column
        action(str): the action method for change document
        fieldnames(list): the fields (headers) in csv file
        count(int): the count of new value that should be changed by count

    Returns:
        returns None

    action methods:
    - int+: adds for integer type
    - int-: substracts value by new_value for integer type
    - str: just adds for string type
    - replace: replaces value by new_value
    """
    data = []
    with open(path, "r", encoding="utf-8") as file:
        reader = csv.DictReader(file, delimiter=";")

        for i, row in enumerate(reader):
            if i == index:
                if action == "int+":
                    row[column] = int(row[column]) + (new_value * count)
                elif action == "int-":
                    row[column] = int(row[column]) - (new_value * count)
                elif action == "str":
                    if row[column]:
                        row[column] += "," + ",".join([new_value] * count)
                    else:
                        row[column] += ",".join([new_value] * count)
                elif action == "replace":
                    row[column] = new_value
            data.append(row)

    with open(path, "w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames, delimiter=";")
        writer.writeheader()
        writer.writerows(data)


def new_product(file_path: str, fields: list, result: dict, delimiter=";") -> None:
    with open(file_path, "a", encoding="utf-8", newline="") as file:
        writer = csv.DictWriter(file, fields, delimiter=delimiter)

        writer.writerow(result)


"""
Class Store
"""


class Store:
    purchases = []

    def __init__(self, name, password, email, card_code, card_balance, is_admin):
        self.name = name
        self.password = password
        self.email = email
        self.card_code = card_code
        self.card_balance = card_balance
        self.is_admin = int(is_admin)

    @classmethod
    def register(cls, name, email, password, card_code, card_balance, is_admin):
        USERS = get_csvdata("users.csv")

        for user in USERS:
            if email != user["email"] and user["password"] != password:
                continue
            else:
                return "User is alredy registered, please try to set other name and password!"

        if not (name and email and password and card_balance and card_code):
            return "Empty values were given."

        if (
            isinstance(name, str)
            and "@" in email
            and len(password) >= 6
            and len(card_code) == 16
        ):
            user_id = int(list(get_csvdata("users.csv"))[-1]["id"]) + 1

            with open("users.csv", "a", newline="", encoding="utf-8") as user_write:
                user_writer = csv.DictWriter(
                    user_write,
                    fieldnames=get_headers("users.csv"),
                    delimiter=";",
                )
                user_writer.writerow(
                    {
                        "id": user_id,
                        "name": name,
                        "password": password,
                        "email": email,
                        "purchases": "",
                        "card_code": card_code,
                        "card_balance": card_balance,
                        "is_admin": int(is_admin),
                    }
                )
            return cls(name, password, email, card_code, card_balance, is_admin)

    @classmethod
    def login(cls, email, password):
        USERS = get_csvdata("users.csv")

        if not (email and password):
            return "Empty values were given."
        for index, user in enumerate(USERS):
            if user["email"] == email and password == user["password"]:
                cls.purchases = list(get_csvdata("users.csv"))[index][
                    "purchases"
                ].split(",")

                return cls(
                    user["name"],
                    password,
                    email,
                    user["card_code"],
                    int(user["card_balance"]),
                    int(user["is_admin"]),
                )

        return "Wrong email or password"

    def purchase(self, product, count):
        if self.card_balance <= 0:
            return "Not enought balance!"

        PRODUCTS = get_csvdata("products.csv")
        USERS = get_csvdata("users.csv")

        for index, user in enumerate(USERS):
            if user["email"] == self.email and user["password"] == self.password:
                for i, pr in enumerate(PRODUCTS):
                    product_name = pr.get("product_name")
                    product_price = int(pr.get("price")) * count

                    try:
                        balance = int(user.get("card_balance"))
                    except (ValueError, TypeError) as error:
                        return error("Wrong credential for card balance!")

                    self.card_balance = balance

                    if (
                        product_name == product
                        and self.card_balance - product_price >= 0
                        and count != 0
                        and count <= int(pr["count"])
                    ):
                        self.card_balance -= product_price

                        user_headers = get_headers("users.csv")
                        # substracting user balance in csv file
                        update_csv(
                            "users.csv",
                            index,
                            "card_balance",
                            product_price,
                            action="int-",
                            fieldnames=user_headers,
                        )
                        # adding product to user csv purchases and class's purchase list
                        update_csv(
                            "users.csv",
                            index,
                            "purchases",
                            product,
                            action="str",
                            fieldnames=user_headers,
                            count=count,
                        )
                        set_user_purchases = list(get_csvdata("users.csv"))[index][
                            "purchases"
                        ].split(",")
                        self.purchases = set_user_purchases
                        # substracting product quantity for every purchase
                        update_csv(
                            "products.csv",
                            i,
                            "count",
                            count,
                            action="int-",
                            fieldnames=get_headers("products.csv"),
                        )
                        all_purchases = "\n\t".join(self.purchases)
                        return f"\n\nSuccessfull! Balance: {self.card_balance}\n{user['name']} purchases:\n\t{all_purchases}"
        return "Not available! Check your balance or the product you has submit."

    def add_product(self, product, count, price, color):
        if self.is_admin:
            product_id = int(list(get_csvdata("products.csv"))[-1]["id"]) + 1

            new_product(
                "products.csv",
                fields=get_headers("products.csv"),
                delimiter=";",
                result={
                    "id": product_id,
                    "product_name": product,
                    "count": count,
                    "price": price,
                    "color": color,
                },
            )
            return "Successfully added new product!"
        return "Please, try again! Enter admin password or email!"


# method = input("Chose method: login/register: ")
# if method.lower() == "login":
#     user_admin = Store.login("emma@emma.com", "23kjdodfkdjsof")
#     print(user_admin.add_product("shirt", 20, 100, "yellow"))
#     user_1 = Store.login("strange@gmail.com", "slkjdf89889")
#     s = time.time()
#     print(user_1.purchase("sweater", 3), f"{time.time()-s:8f}")
# elif method.lower() == "register":
#     user_2 = Store.register(
#         "John", "john@john.com", "dfsfsafsdfasdf", "4657675849586758", 12000, False
#     )
#     print(user_2.add_product("shirt", 30, 100, "white"))
#     s = time.time()
#     print(user_2.purchase("sweater", 1), f"{time.time()-s:8f}")
