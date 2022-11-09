# **********
# *        * 
# *        * 
# **********


length = 4
width = 10
star = '*'
i = 0
while i < length:
    if i > 0 and i < (length - 1): 
        empty = ' ' * (width - 2)
        print(f'{star}{empty}{star}')
    else:
        print(star * width)
    i += 1


# square_line = 4 
# star = "*" 
# for i in range(square_line):
#     if i > 0 and i < (square_line - 1):
#         empty = ' ' * (square_line - 2)
#         print(f'{star}{empty}{star}')
#     else:
#         print(star * square_line)