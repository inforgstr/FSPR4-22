# # any_argument(2, 3, 4, 5, 6, 'dfd', [3, 4])


# # Правило передачи аргуиентов
# def order_of_args(name, default='go', *args, username, sep='separator', end='\n', **kwargs):
#     print(name, default, args, username, sep, end, kwargs)

# order_of_args('Behruz', 123, 4, 5, 6, username='apo', end='not enter', none='key', key='value', email='e@com', loot=[3, 4])


# def func_values(*n, **u):
#     return (n, u)

# print(func_values(2, 3, [5], user={'name': ''}))


def shades_of_grey(n):
    shades = []
    hex = '0123456789abcdef'
    counter = 0
    b = 0
    if 0 <= n <= 254:
        for i in range(n+1):
            if counter ==  16:
                counter = 0
                b += 1
            gray = f'#0{hex[counter]}0{hex[counter]}0{hex[counter]}'
            if i == 16:
                gray = f'#{hex[b]}{hex[0]}{hex[b]}{hex[0]}{hex[b]}{hex[0]}'
            if i >= 17:
                gray = f'#{hex[b]}{hex[counter]}{hex[b]}{hex[counter]}{hex[b]}{hex[counter]}'
            shades.append(gray)

            counter += 1
    elif 254 <= n:
        for i in range(255):
            
            if counter ==  16:
                counter = 0
                b += 1
            gray = f'#0{hex[counter]}0{hex[counter]}0{hex[counter]}'
            if i == 16:
                gray = f'#{hex[b]}{hex[0]}{hex[b]}{hex[0]}{hex[b]}{hex[0]}'
            if i >= 17 or i <= 256:
                gray = f'#{hex[b]}{hex[counter]}{hex[b]}{hex[counter]}{hex[b]}{hex[counter]}'
            shades.append(gray)

            counter += 1

    if shades:
        shades.pop(0)
        return shades
    elif n < 0:
        return []
    else:
        return shades

print(shades_of_grey(255))