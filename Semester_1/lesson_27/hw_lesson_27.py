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
    purchases = []
    def __init__(self, name, email, password, card_code, card_balance):
        self.name = name
        self.email = email
        self.password = password
        self.card_code = card_code
        self.card_balance = card_balance

    @classmethod
    def login(cls, email, password):
        if not(email and password):
            return 'Empty values were given.'
        for user in USERS:
            if user['email'] == email and user['password'] == password:
                return cls(user['name'], email, password, user['card']['code'], user['card']['money'])
            else:
                return 'Wrong email or password'

    @classmethod
    def register(cls, name, email, password, card_code, card_balance):
        for user in USERS:
            if email != user['email'] and user['password'] != password:
                break
            else:
                return 'Wrong email and password.'
        if not(name and email and password and card_code and card_balance):
            return 'Empty values were given.'
        if isinstance(name, str) and '@' in email and len(password) >= 6 and len(card_code) == 16:
            USERS.append(
                {
                    'name': name,
                    'password': password,
                    'email': email,
                    'purchases': [],
                    'card': {'code': card_code, 'money': card_balance}
                }
            )
            return cls(name, email, password, card_code, card_balance)

    def purchase(self, product):
        if product not in PRODUCTS.keys():
            return 'Not available!'
        for i, val in PRODUCTS.items():
            if i == product and self.card_balance - val >= 0:
                self.card_balance -= val
                self.purchases.append(product)
                USERS[-1]['purchases'].append(product)
                return f'\nSuccesfully bought {product} and added in purchases!\nBalance: {self.card_balance}\nYour purchases {self.purchases}'
            elif self.card_balance - val < 0:
                return 'Not enough money.'


enter = input('register or login: ')
if enter == 'login':
    user_1 = Store.login('behruz@gmail.com', '234fjfdsd')
    print(user_1.purchase('wear'))
elif enter == 'register':
    user_1 = Store.register('H', 'sdfsfds@gmail.com', 'sdfdsdflsdf', '6475869957688909', 1000)
    print(user_1.purchase('key'))
    user_2 = Store.register('B', 'dfsd@gmail', 'sdflkjsldfs', '7685768857689878', 500)
    print(user_2.purchase('wear'))
    