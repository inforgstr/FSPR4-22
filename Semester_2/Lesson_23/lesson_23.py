# USERS = []


# def register(name, email, password, card_code, card_balance):
#     """Регистрация и создание пользования.

#     Большое описание на 120 и более символов.

#     Args:
#         name (str): Имя пользователя
#         email (str): dfgh
#         password (str): adsd
#         card_code (str): sdasd
#         card_balance (int): qwerth

#     Returns:
#         Store class instance
#     """
#     # Есть ли данный пользователь в системе
#     try:
#         for user in USERS:
#             if user["email"] == email and user["password"] == password:
#                 return "Пользователь с такими данными уже есть."
        
#         if not (name and email and password and card_code and card_balance):
#             return "Empty values were given."
    

#         if (
#             name.isalpha()
#             and "@" in email
#             and len(password) >= 6
#             and len(card_code) == 16
#             and card_balance >= 0
#         ):
#             USERS.append(
#                 {
#                     "name": name,
#                     "password": password,
#                     "email": email,
#                     "purchases": [],
#                     "card": {"code": card_code, "balance": card_balance},
#                 }
#             )
#             return (name, email, password, card_code, card_balance)
#     except (TypeError, AttributeError):
#         return "Please, input correct data!"
    
#     else:
#         return "Wrong credentials!"
#     finally:
#         print("Your code has completed without exceptions!\n")

# # try:
# print(register("sldkfj", "d@gmail.com", "342399", "5657584459684758", 12))
# # except TypeError as ex:
# #     print("Argument required:", ex)


# class UserAgeIsLessThanEighteen(Exception):
#     """The user should be anove 18."""

# user = {
#     "age": 12,
# }

# if user["age"] < 18:
#     raise UserAgeIsLessThanEighteen()

# class IsUsernameLengthGreaterThanThree(Exception):
#     """Username should be greater than three."""
#     print("Username should be greater than three!")

# user = {
#     "username": "ea",
# }
# try:
#     if len(user["username"]) > 3:
#         print("Success!")
# except IsUsernameLengthGreaterThanThree as ex:
#     print(ex)


# def map_2(func, *iterable):
#     d = {}

#     min_length = min([len(x) for x in iterable])

#     for iter in iterable:
#         for i in range(min_length):
#             if i in d:
#                 d[i].append(iter[i])
#             else:
#                 d[i] = [iter[i]]

#     return [func(*d[variable]) for variable in d]
# lst = [1, 2]

# print(next(map(lambda x:x+1, lst)))
# print(list(iter(map(lambda x:x+1, lst))))
# print(list(iter(map(lambda x:x+1, lst))))

# dog_foods = {
#     "dasfas": 2,
#     "kjsdf": 23,
#     "lksjdfsdf": 324,
# }

# dog_foods_iter = iter(dog_foods)

# while True:
#     try:
#         print(next(dog_foods_iter))
#     except StopIteration:
#         break


# range_iter = iter(range(100000))

# while True:
#     try:
#         print(next(range_iter))
#     except StopIteration:
#         break
