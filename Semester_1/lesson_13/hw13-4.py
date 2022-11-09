# def shades_of_grey(n):
#     shades = []
#     hex = '0123456789abcdef'
#     counter = 0
#     b = 0
#     if 0 <= n <= 254:
#         for i in range(n+1):
        
#             if counter ==  16:
#                 counter = 0
#                 b += 1

#             gray = f'#0{hex[counter]}0{hex[counter]}0{hex[counter]}'


#             if i == 16:
#                 gray = f'#{hex[b]}{hex[0]}{hex[b]}{hex[0]}{hex[b]}{hex[0]}'


#             if i >= 17:
#                 gray = f'#{hex[b]}{hex[counter]}{hex[b]}{hex[counter]}{hex[b]}{hex[counter]}'


#             shades.append(gray)

#             counter += 1
#     elif 254 <= n:
#         for i in range(255):
            
#             if counter ==  16:
#                 counter = 0
#                 b += 1

#             gray = f'#0{hex[counter]}0{hex[counter]}0{hex[counter]}'


#             if i == 16:
#                 gray = f'#{hex[b]}{hex[0]}{hex[b]}{hex[0]}{hex[b]}{hex[0]}'


#             if i >= 17 or i <= 256:
#                 gray = f'#{hex[b]}{hex[counter]}{hex[b]}{hex[counter]}{hex[b]}{hex[counter]}'


#             shades.append(gray)

#             counter += 1


        
#     if shades:
#         shades.pop(0)
#         return shades
#     elif n < 0:
#         return []
#     else:
#         return shades

# print(shades_of_grey(int(input())))


def f(n):
    '''If no argument is given, the constructor creates a new empty list.
        The argument must be an iterable if specified'''
    shades = []
    second = '0123456789abcdef'
    first = '0123456789abcdef'
    if n < 0:
        return shades
    counter = 0
    for i in range(n//10+1): 
        if counter == 16: # 0 1 2 3 4 5 6 7 ...
            counter = 0
            # 11            11
        # if (n + 1) == len(shades) or len(shades) == 255: # 0 1 2 3
        #     break
        for _ in range(16):
            if (n + 1) == len(shades) or len(shades) == 255:
                break
            h = f'#{first[counter]}{second[_]}{first[counter]}{second[_]}{first[counter]}{second[_]}'
            shades.append(h)
        counter += 1

    if shades:
        shades.pop(0)

    return shades

print(f(70))