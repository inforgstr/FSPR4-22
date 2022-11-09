user_login = input('Введите логин: ')
user_age = int(input('Введите свой возраст: '))

if user_age >= 18:
    print(user_login.title() + ' you have succesfully registered!')
else:
    print(user_login.title() + ' you have not registered, yet!')