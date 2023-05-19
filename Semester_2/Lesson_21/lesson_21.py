# def hello():
#     print("Hello, World!")


# def my_decorator(func):
#     def wrapper():
#         print("Changing...")
#         func()
#         print("Changing...")
#     return wrapper


# answer = my_decorator(hello)
# print(answer)
# print(answer())


# @authorize
# def like():
#     print("Greetings")

# like()


# def authorize(func):
#     def wrapper(*args, **kwargs):
#         print("Changes...")
#         print("Changes...")
#         return func(*args, **kwargs)

#     return wrapper


# @authorize
# def like():
#     print("Greetings")


# @authorize
# def buy(item, price):
#     return item * price


# print("total =", buy(2, 290))



