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
        'card' : {'code': '3647583465734283', 'money': 1000}
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

class StoreOwner:
    def __init__(self, name, value, color):
        self.name = name
        self.value = value
        self.color = color
    
    @classmethod
    def remove_product(cls, name, value):
        '''
        Removes information of product

        Args:
            name: str
            value: int
        '''

        if not(name and value):
            return 'Empty values were given.'

        for id, product in enumerate(PRODUCTS):
            if product['name'] == name and product['value'] == value:
                PRODUCTS.pop(id)
                return cls(name, value, product['color'])
        return 'Wrong name or value of product.'

    @classmethod
    def adding_product(cls, name, value, color):
        '''
        Adds product's data to PRODUCTS

        Args:
            name: str
            value: int
            color: str
        '''
        if not (name and value and color):
            return 'Empty values were given.'
        
        if name.isalpha() and isinstance(value, int) and color.isalpha():
            PRODUCTS.append(
                {
                    'name': name,
                    'value': value,
                    'color': color,
                }
            )
            return cls(name, value, color)
        
    @classmethod 
    def modify_product(cls, name_default, value_default, name, value, color):
        '''
        Changes information of product
        
        Args:
            name_default: str
            value_default: int
            name: str
            value: int
            color: str
        '''
        if not (name_default and value_default and name and value and color):
            return 'Empty values were given.'
        
        for id, product in enumerate(PRODUCTS):
            if product['name'] == name_default and product['value'] == value_default:
                PRODUCTS[id]['name'] = name
                PRODUCTS[id]['value'] = value
                PRODUCTS[id]['color'] = color
                return cls(name, value, color)
        return 'Wrong credentials.'

admin = StoreOwner.remove_product('wear', 100)
print(PRODUCTS)
admin = StoreOwner.adding_product('car', 10000, 'black')
print(PRODUCTS)
admin = StoreOwner.modify_product('car', 10000, 'car', 12000, 'white')
print(PRODUCTS)
admin = StoreOwner.modify_product('car', 12000, 'electro-car', 15000, 'white')
print(PRODUCTS)