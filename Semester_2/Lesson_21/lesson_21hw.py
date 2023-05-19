# Nested lists with recursive function

# lst = [2, [2, 3, [[[[[[[[5]]]]]]]]]]


# def num_nests(array, n=0):
#     if n == len(array):
#         return 0
#     elif isinstance(array[n], list):
#         return 1 + num_nests(array[n])
#     return num_nests(array, n + 1)


# print(num_nests(lst))


data = {
    "users": [
        {
            "username": "user_1",
            "password": 1002030,
        },
        {
            "username": "user_2",
            "password": 1532124,
        },
        {
            "username": "user_3",
            "password": 5231423,
        },
    ],
    "products": [
        {
            "name": "Phone",
            "quantity": 30,
            "price": 1000,
        },
        {
            "name": "Laptop",
            "quantity": 15,
            "price": 2500,
        },
        {
            "name": "Bag",
            "quantity": 100,
            "price": 200,
        },
    ],
}


def authorize(username, password):
    def decorator_authorize(func):
        def wrapper(*args, **kwargs):
            for item in data["users"]:
                if item["username"] == username and item["password"] == password:
                    return func(*args, **kwargs)
                else:
                    return "Wrong credentials!\n\nPlease, check your data and resubmit your purchase!"

        return wrapper

    return decorator_authorize


@authorize(username="user_1", password=1002030)
def buy(name: str, amount: int, price: int) -> str:
    for item in data["products"]:
        if (
            name == item["name"]
            and price >= item["price"]
            and amount <= item["quantity"]
        ):
            return f"Successful, for {name}! Your purchase has bought!\nYour remainder - {price-item['price']} $."
        else:
            return "Wrong credentials!\n\nPlease, check your data and resubmit your purchase!"


print(buy("Phone", 30, 2000))
