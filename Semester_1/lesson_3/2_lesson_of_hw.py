'''
Методы:
-- Capitalize()
-- Find()
-- Index()
-- Isdigit()
-- Lower()
-- Upper()
-- Join()
'''
# Применение метода -- capitalize()
message = 'happy birthday!'
print(message.capitalize())

# Применение метода -- find()
message = 'happy birthday!'
print(message.find('p'))

# Применение метода  -- index()
message = 'Please, recall me...'
print(message.index('r'))

# Применение метода -- isdigit()  (True)
message = '48454548'
print(message.isdigit())

# Применение метода -- isdigit() (False)
message = '484545sfgs48'
print(message.isdigit())

# Применение метода  -- lower()
message = 'Please, recall me...'
print(message.lower())

# + Применение метода -- title()
message = 'PlEAse, reCall mE...'
print(message.title())

# Применение метода -- upper()
message = 'Please, recall me...'
print(message.upper())

# Применение метода -- join()
message = ('Peter', 'John', 'Nick')
message_m = '--'.join(message)
print(message_m)