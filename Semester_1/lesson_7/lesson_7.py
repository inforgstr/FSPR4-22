# set - множество
# нельзя индексировать 
# можно менять через методы или циклы 
numbers = {2, 3, 4, 'hello', 2, 4}
# print(numbers, numbers[0]) # error
print(numbers, numbers)

numbers = {} # dict
# print(type(numbers))
numbers = set()
print(type(numbers))


remove_duplicates = [1, 2, 3, 4, 5, 5, 6, 'AA', 'BB', 'AA']
a = list(set(remove_duplicates))
print(remove_duplicates, list(set(remove_duplicates)), sep='\n')

# tuple(result)  

list
tuple
set
dict




# Итерируемые - iterable. Исчесляемый. Это те переменные, которые хранят больше одного значения 
# Индексы 


names = []
print(type(names))
names = ()

# Dictionary - Словарь
# ключом словарья могут быть только не изменяемые типы пременных 
user_data = {
    'key': "sfds",
    1: None,
    2: 21,
    3: 6.7,
    4: [2, 3, 4],
    5: (1, 2, 3),
    6: {'key' : 'Другой словарь'}
}

#  40-50 sdfs8fsfadfa8sdfasd7fasff5f
# print(type(user_data), user_data['key'], sep='\n')

# print(user_data, user_data[1], user_data[2], user_data[3], user_data[4], user_data[5], user_data[6]['key'], sep='\n')


user_data = {
    'username': 'Gobby', 
    'password': 'sdfsw4', 
    'age': 18,# Нельзя создавать значения с одинаковыми ключами 
    'age': 22 # qweuriyqw4gyiouih3
}


user_data['username'] = 'Alabasta'
print(user_data.keys(), user_data.values(), user_data.items(), sep='\n')




# view
# dict_keys(['username', 'password', 'age'])
# dict_values(['Alabasta', 'sdfsw4', 22])
# dict_items([('username', 'Alabasta'), ('password', 'sdfsw4'), ('age', 22)])

user_list = list(user_data.values())
print(user_data)

# print(user_data['unexisting']) / Ошибка 
print(user_data.get('age'), user_data.get('unexisting'))



user_data = [
    {
        'username': 'Gobby', 
        'password': 'sdfsw4', 
        'age': 18,
    },
    {
        'username': 'Apo', 
        'password': 'sdfsw4sf', 
        'age': 14,
    }
]

# print(user_data[0]['username'], user_data[0]['age'])

