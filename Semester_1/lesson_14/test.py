def f(n):
    '''If no argument is given, the constructor creates a new empty list.
        The argument must be an iterable if specified'''

    
    n = 256
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

print(f(250))