'''
Создать класс с атрибутами: name, email, password, purchases (список), card 
методами: 
- purchase - метод для покупки товаров. 
    Для покупки вам нужно узнать, какой товар хочет купить человек и есть у него достаточно денег для этого. 
    Если условия верны, то человек покупает товар и с его счета снимаются деньги 
    Если товара нет в списке товаров, вывести сообщение что товара нет, если не достаточно денег,  
    то вывести сообщение что не достаточно средств. 
 
- register - создать нового пользователя и включить его в список пользователей если: 
    name - должен содержать только буквы 
    email - должен содержать @ 
    password - миинмальная длинна 6 
    card - длина ключа code была равна 16 
 
    Если все условия прошли, то создать пользователя с атрибутами и записать его данные в переменную USERS. 
 
- login - вход в систему, если пользователь уже есть. При этом пользователь должен иметь все свои данные:  
    покупки, список купленных товаров и т.д 
    Для логина вам нужно узнать, есть ли такой пользователь в системе или нет. Если его нет, то сказать что нужно пройти регистрацию. 
    Если есть, то создать все атрибуты класса из имеющихся данных. 
 
- add_product - добавить куплейнный товар в атрибут purchases.
'''



USERS = [
    {
        'name' : 'Behruz',
        'password' : '234fjfdsd',
        'email' : 'behruz@gmail.com',
        'purchases' : [],
        'card' : {'code': '3647583465734283', 'money': 1000}
    }
]
PRODUCTS = {
    'key' : 3,
    'wear' : 200,
}


class Store:
    a = input('login or register: ')
    if a == 'login':
        def __init__(self, name=input('Input your account\'s name: '), password=input('Input your account\'s password: '), email=input('Input your email: '), purchases=[], card=input('Input the correct code of your card: ')):
            if name == USERS[0]['name'] and password == USERS[0]['password'] and email == USERS[0]['email'] and card == USERS[0]['card']['code']:
                print('You have succesfully loged in!')
            else:
                print('Your account have not found in our server! You need to register!')


            self.name = name 
            self.password = password
            self.purchases = purchases
            self.email = email 
            self.card = card

        def purchase(self, product):
            value = USERS[0]['card']['money']
            if product not in PRODUCTS.keys():
                print('\nNot available!')
            for i, val in PRODUCTS.items():
                if i == product and value - val > 0:
                    value -= val
                    print(f'\nYou have succesfully bought this product. You lost {val}. And you left {value-val}')
                elif value - val <= 0:
                    print('\nNot enough money!')
        
    elif a == 'register':

        USERS.append(USERS[0].copy())
        USERS[1].pop('card')

        def __init__(self, name=input('Input your name: '), password=input('Create a new password: '), email=input('Input your email: '),  purchases=[], card=input('Input the correct code of your card: ')):
            if USERS[0]['name'] != name:
                if isinstance(name, str) and '@' in email and len(password) > 6 and len(card) == 16:
                    USERS[1]['name'] = name
                    USERS[1]['password'] = password
                    USERS[1]['email'] = email
                    USERS[1].update({'card': {'code':card, 'money': 1000}})
                    
                else:
                    print('\nIncorrect type of password or email or card, please try again!')
            else:
                print('\nYou have registered! Please try again.(WARNING! You should log in!)')
            self.name = name
            self.password = password
            self.email = email
            self.card = card
            self.purchases = purchases
        
        def purchase(self, product):
            value = USERS[1]['card']['money']
            if product not in PRODUCTS.keys():
                print('\nNot available!')

            for i, val in PRODUCTS.items():
                if i == product and value - val > 0:
                    value -= val
                    print(f'\nYou have succesfully bought this product. You lost {val}. And you left {value-val}.')
                    purchased = product
                    self.purchases.append(purchased)
                    print(f'Automatically added {purchased} in purchases.')
                    
                elif value - val < 0:
                    print('\nNot enough money!')

            


store = Store()
store.purchase('wear')


