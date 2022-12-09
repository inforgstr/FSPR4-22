'''
1. Кодварс три любые три задачи
2. Создать класс StoreOwner для работы с продуктами. Должен иметь возможность удаления, 
    добавления и изменения данных о продукте(ах) и пользователей.
'''
USERS = [
    {
        'name' : 'Behruz',
        'password' : '234fjfdsd',
        'email' : 'behruz@gmail.com',
        'purchases' : [],
        'card' : {'code': '3647583465734283', 'balance': 1000}
    }
]

PRODUCTS = [
    {
        'name': 'key',
        'value': 5,
        'color': 'black',
    },
    {
        'name': 'wear',
        'value': 100,
        'color': 'white',
    }
]

#                        STORE

# class Store:
#     purchases = []
#     def __init__(self, name, email, password, card_code, card_balance):
#         self.name = name
#         self.email = email
#         self.password = password
#         self.card_code = card_code
#         self.card_balance = card_balance

#     @classmethod
#     def login(cls, email, password):
#         if not(email and password):
#             return 'Empty values were given.'
#         for user in USERS:
#             if user['email'] == email and user['password'] == password:
#                 return cls(user['name'], email, password, user['card']['code'], user['card']['money'])
#         return 'Wrong email or password'

#     @classmethod
#     def register(cls, name, email, password, card_code, card_balance):
#         for user in USERS:
#             if email == user['email'] and user['password'] == password:
#                 return 'User with this name and email is in data!'

#         if not(name and email and password and card_code and card_balance):
#             return 'Empty values were given.'
#         if isinstance(name, str) and '@' in email and len(password) >= 6 and len(card_code) == 16:
#             USERS.append(
#                 {
#                     'name': name,
#                     'password': password,
#                     'email': email,
#                     'purchases': [],
#                     'card': {'code': card_code, 'money': card_balance}
#                 }
#             )
#             return cls(name, email, password, card_code, card_balance)
#         return 'Wrong email or password!'

#     def purchase(self, product):
#         for PRODUCT in PRODUCTS:
#             if product not in PRODUCT.keys():
#                 return 'Not available!'
#             for i, val in PRODUCT.items():
#                 if i == product and self.card_balance - val >= 0:
#                     self.card_balance -= val
#                     self.purchases.append(product)
#                     for id, user in enumerate(USERS):
#                         if user['email'] == self.email and user['password'] == self.password:
#                             USERS[id]['purchases'].append(product)
#                     PRODUCT.pop(i)
#                     return f'\nSuccesfully bought {product} and added into purchases!\nBalance: {self.card_balance}\nYour purchases: {self.purchases}'
                    
#                 elif self.card_balance - val < 0:
#                     return 'Not enough money.'

# enter = input('register or login: ')
# if enter == 'login':
#     user_1 = Store.login('behruz@gmail.com', '234fjfdsd')
#     if isinstance(user_1, Store):
#         print(user_1.purchase('wear'))
#     else:
#         print('Wrong email or password!')

# elif enter == 'register':
#     user_1 = Store.register('H', 'sdfsfdsgmail.com', 'sdfdsdflsdf', '6475869955688909', 1000)
#     user_2 = Store.register('B', 'dfsd@gmail', 'sdflkjsldfs', '7685768857689878', 500)

#     if isinstance(user_1, Store):
#         print(user_1.purchase('wear'))
#     if isinstance(user_2, Store):
#         print(user_2.purchase('key'))
#     else:
#         print('Wrong data\'s were given!')





#                        CLASS STOREOWNER

class StoreOwner:
    def __init__(self, name_of_product, value_of_product, color_of_product):
        self.name = name_of_product
        self.value = value_of_product
        self.color = color_of_product
    
    @classmethod
    def remove_product(cls, name_of_product, value_of_product):
        '''
        Removes information of product

        Args:
            name: str
            value: int
        '''

        if not(name_of_product and value_of_product):
            return 'Empty values were given.'

        for id, product in enumerate(PRODUCTS):
            if product['name'] == name_of_product and product['value'] == value_of_product:
                PRODUCTS.pop(id)
                return cls(name_of_product, value_of_product, product['color'])
        return 'Wrong name or value of product.'

    @classmethod
    def adding_product(cls, name_of_product, value_of_product, color_of_product):
        '''
        Adds product's data to PRODUCTS

        Args:
            name: str
            value: int
            color: str
        '''
        if not (name_of_product and value_of_product and color_of_product):
            return 'Empty values were given.'
        
        if name_of_product.isalpha() and isinstance(value_of_product, int) and color_of_product.isalpha():
            PRODUCTS.append(
                {
                    'name': name_of_product,
                    'value': value_of_product,
                    'color': color_of_product,
                }
            )
            return cls(name_of_product, value_of_product, color_of_product)
        
    @classmethod 
    def modify_product(cls, name_default_product, value_default_product, name_of_product, value_of_product, color_of_product):
        '''
        Changes information of product
        
        Args:
            name_default: str
            value_default: int
            name: str
            value: int
            color: str
        '''
        if not (name_default_product and value_default_product and name_of_product and value_of_product and color_of_product):
            return 'Empty values were given.'
        
        for id, product in enumerate(PRODUCTS):
            if product['name'] == name_default_product and product['value'] == value_default_product:
                PRODUCTS[id]['name'] = name_of_product
                PRODUCTS[id]['value'] = value_of_product
                PRODUCTS[id]['color'] = color_of_product
                return cls(name_of_product, value_of_product, color_of_product)
        return 'Wrong credentials.'



    def modify_user(self, default_email, default_password, name_user, password_user, email_user, card_code_user, card_balance_user):
        '''
        Changes user's data.


        Args:
            default_email: str
            default_password: str
            name: str
            password: str
            email: str
            card_code: str
            card_balance: int
        '''
        if not(default_email and default_password and name_user and password_user and email_user and card_code_user and card_balance_user):
            return "Empty values were given."

        for id, user in enumerate(USERS):
            if user['email'] == default_email and user['password'] == default_password:
                if isinstance(name_user, str) and '@' in email_user and len(password_user) >= 6 and len(card_code_user) == 16:
                    USERS[id]['name'] = name_user
                    USERS[id]['password'] = password_user
                    USERS[id]['email'] = email_user
                    USERS[id]['card']['code'] = card_code_user
                    USERS[id]['card']['balance'] = card_balance_user
        return 'Wrong credentials.'


admin = StoreOwner.remove_product('wear', 100)
print(PRODUCTS)
admin = StoreOwner.adding_product('car', 10000, 'black')
print(PRODUCTS)
admin = StoreOwner.modify_product('car', 10000, 'car', 12000, 'white')
print(PRODUCTS)
admin = StoreOwner.modify_product('car', 12000, 'electro-car', 15000, 'white')
print(PRODUCTS)
admin.modify_user('behruz@gmail.com', '234fjfdsd', 'N', 'kljdsfsd8', 'lsjf@gmail.com', '7485988767789899', 800)
print(USERS)