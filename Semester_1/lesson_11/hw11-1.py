#     *
#    ***
#   *****
#  *******
# ********* 
#     *
#     *


length = 6
width = length + 1
star = '*' 
spaces = length - 4
stars = length - 3

for i in range(length): # 0 1 2 3 4 5 6
    if i > 0 and i < (length - 3): # 1 2 3
        print(' ' * spaces + star * stars)
        for n in range(i):
            stars += 2
            spaces -= 1
            for i in range(n):
                spaces += 1
        
    elif i == (length - 3):
        print(star * width)
        
    else:
        print(int((width) / 2) * ' ' + star)