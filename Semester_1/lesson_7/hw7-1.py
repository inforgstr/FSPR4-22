'''
Methods of set:

    union 
    update 
    add
    pop 
    remove 
    copy
    clear
    difference
'''

#  Method - union()
first_user = {'coffee', 'water', 'beverage'}
second_user = {'water', 'apple', 'banana'}
third_user = {'coffee', 'apple', 'beverage', 'meal'}

wishes = first_user.union(second_user, third_user)
print(wishes, '\n')

#  Method - update()
first_user = {'apple', 'miilk', 'bag'}
second_user = {'coffee', 'apple', 'beverage', 'meal'}
first_user.update(second_user)
print(first_user, '\n')

# Method - add()
user_login = {'meal', 'dog', 'cat', 'parrot'}
user_login.add('pet')

print(user_login, '\n')

# Method - pop()
user = {'apples', 'pets', 'parrots', 'meal', 'dog', 'cat', 'parrot'}
user_password = user.pop()
print(user, ' ', user_password, '\n')

# Method - remove()
user = {'meal', 'dog', 'cat', 'parrot'}
user.remove('meal')
print(user)

# Method - copy()
user = {'meal', 'dog', 'cat', 'parrot'}
user_login = user.copy()
print(user, ' = ', user_login)

# Method - clear()
user = {'apples', 'pets', 'parrots', 'meal', 'dog', 'cat', 'parrot'}
user.clear()
print(type(user), user)

# Method - difference()
user_login = {'apples', 'pets', 'parrots', 'meal', 'dog', 'cat', 'parrot'}
user_login1 = {'meal', 'dog', 'cat', 'parrot'}
user_password = user_login.difference(user_login1)
print('\n', user_password)