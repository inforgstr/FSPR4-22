# Comperhension

numbers = []
for i in range(10):
    numbers.append(i)
# print(numbers)

def multiply(i):
    return i * 5

numbers = [i * 5 for i in range(10)]
print(numbers)

numbers = [i * 5 for i in range(10) if i > 5]
print(numbers)


numbers = [i*5 if i > 5 else False for i in range(10)]
print(numbers)

message = (('Hi', 'Steve!'), ('What\'s', 'up?'))
print([word for sentence in message for word in sentence])

numbers = (i * 5 for i in range(10)) # generator
print(numbers)

numbers = tuple(i * 5 for i in range(10)) # type tuple()
print(numbers)

numbers = {i * 5 for i in range(10)} # set
print(numbers)

numbers = {i:i*5 for i in range(10)} # dict
print(numbers)








