'''
Применение методов в списках:

    append
    count 
    copy
    insert
    sort 
    extend
    pop
    index

'''
# method - append
part1 = []
part1.append('bmw')
part1.append('audi')
part1.append('iphone')
print('\n\nMethod - append():\n\t\t', part1)

part2 = ['city', '45', 'street']
part3 = ['suzuki', '34', 'rocket']
part2.append(part3)
print('\t\t', part2)

# method - count
message = ['audi', 'bmw', 'yamaha', 'bmw']
a = message.count('bmw')
print('\n\nMethod - count():\n\t\t', a)

message = [1, 2, 3, 4, 5, 6, 4, 3, 5, 5, 5, 6, 7, 7, 5, 5, 4, 4]
print('\t\t', message.count(5))

# method - copy
message = ['audi', 'bmw', 'yamaha', 'bmw']
print('\n\nMethod - copy():\n\t\t', message.copy())

# method - insert
message = ['audi', 'bmw', 'yamaha', 'bmw']
message.insert(0, 'iphone')
message.insert(5, 'bugati')
print('\n\nMethod - insert():\n\t\t', message)

# method - sort - alphabetically
message = ['bmw', 'yamaha', 'audi', 'bmw']
message.sort()
print('\n\nMethod - sort():\n\t\t', message)

# or 

message.sort(reverse=True)
print('\n\nMethod - sort() with reverse alphabetically:\n\t\t', message)



# method - sorted 
text = ['cars', 'toys', 'buildings', 'helicopters']
print('\n\n\t\tMethod sorted()')
print('\n\nOriginal list: ')
print(text)

print('\nSorted list:')
print(sorted(text))

print('\nOriginal list again: ')
print(text, '\n\n')


# method - extend
tech = ['data', 'server', 'computer']
numbers = [1, 3, 34, 5453, 34535, 23]
tech.extend(numbers)
print('\n\nMethod - extend()\n\t\t', tech)

# method - pop
message1 = ['ads', 'adverts', 'marketing']
message2 = message1.pop(0)
print('\n\nMethod - pop():\n\t\t', message1)

# method - index
mes = [23, 234, 43, 567, 677, 6756, 567, 676, 676,]
a = mes.index(677)
print('\n\nMethod - index():\n\t\t', a)