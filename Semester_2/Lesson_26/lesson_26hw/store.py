import csv


# get list of exact file
def get_csv(file_path: str, delimiter: str) -> list[dict]:
    with open(file_path, "r") as reader:
        return list(csv.DictReader(reader, delimiter=delimiter))


# update for column by index to set new value
def update_csv_file(
    path: str, index: int, column: str, new_value, action, fieldnames, count=1
) -> None:
    with open(path, "r") as file:
        reader = csv.DictReader(file, delimiter=";")
        data = list(reader)

    if action == "int+":
        data[index][column] = int(data[index][column]) + (int(new_value) * count)
    elif action == "int-":
        data[index][column] = int(data[index][column]) - (int(new_value) * count)

    elif action == "str" and data[index][column]:
        data[index][column] += "," + ",".join([new_value] * count)
    else:
        data[index][column] += ",".join([new_value] * count)

    with open(path, "w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames, delimiter=";")
        writer.writeheader()
        writer.writerows(data)


class Store:
    purchases = []

    def __init__(self, name, password, email, card_code, card_balance):
        self.name = name
        self.password = password
        self.email = email
        self.card_code = card_code
        self.card_balance = card_balance

    @classmethod
    def register(cls, name, email, password, card_code, card_balance):
        USERS = get_csv("users.csv", ";")

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
            with open("users.csv", "a", newline="") as user_write:
                user_id = int(USERS[-1]["id"]) + 1

                user_writer = csv.DictWriter(
                    user_write,
                    fieldnames=list(USERS[0].keys()),
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
                    }
                )
            return cls(name, password, email, card_code, card_balance)

    @classmethod
    def login(cls, email, password):
        USERS = get_csv("users.csv", ";")

        if not (email and password):
            return "Empty values were given."
        for index, user in enumerate(USERS):
            if user["email"] == email and password == user["password"]:
                cls.purchases = get_csv("users.csv", delimiter=";")[index][
                    "purchases"
                ].split(",")

                return cls(
                    user["name"],
                    password,
                    email,
                    user["card_code"],
                    int(user["card_balance"]),
                )

        return "Wrong email or password"

    def purchase(self, product, count):
        if self.card_balance <= 0:
            return "Not enought balance!"

        PRODUCTS = get_csv("products.csv", ";")
        USERS = get_csv("users.csv", ";")

        for index, user in enumerate(USERS):
            if user["email"] == self.email and user["password"] == self.password:
                for i, pr in enumerate(PRODUCTS):
                    product_name = pr.get("product_name")
                    product_price = int(pr.get("price")) * count
                    balance = int(user.get("card_balance"))
                    self.card_balance = balance

                    if (
                        product_name == product
                        and self.card_balance - product_price >= 0
                        and count != 0
                        and count <= int(pr["count"])
                    ):
                        self.card_balance -= product_price

                        users_header = list(USERS[0].keys())
                        # substracting user balance in csv file
                        update_csv_file(
                            "users.csv",
                            index,
                            "card_balance",
                            product_price,
                            action="int-",
                            fieldnames=users_header,
                        )
                        # adding product to user csv purchases and class's purchase list
                        update_csv_file(
                            "users.csv",
                            index,
                            "purchases",
                            product,
                            action="str",
                            fieldnames=users_header,
                            count=count,
                        )
                        set_user_purchases = get_csv("users.csv", delimiter=";")[index][
                            "purchases"
                        ].split(",")
                        self.purchases = set_user_purchases
                        # substracting product quantity for every purchase
                        update_csv_file(
                            "products.csv",
                            i,
                            "count",
                            count,
                            action="int-",
                            fieldnames=list(PRODUCTS[0].keys()),
                        )
                        all_purchases = "\n\t".join(self.purchases)
                        return f"\n\nSuccessfull! Balance: {self.card_balance}\n{user['name']} purchases:\n\t{all_purchases}"
        return "Not available! Check your balance or the product you has submit."
