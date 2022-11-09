def func(a, default='hi'):
    print(a, default)

# func(12)
# func(12, 'not hi')

def func(a, b, default='hi'):
    print("a = ", a, "b = ", b, default)

# func(12, 4)
# func(b=12, a=4)
# func(12, 5, "not hi")

# args
def func(a, b, default="hi", *args):
    print(a, b, 'default = ', default, 'args = ', args)

# func(12, 4, 'yeey', 3, 4, [2, 3, 4])

def any_arg(*ars):
    """Function accepts any arguments and return it on screen"""
    print('args = ', ars)
    for ar in ars:
        print(ar)

any_arg(2, 3, 4, 'gooooo', 'noooooooo', {1: 1}, True, [], {3, 4, 5, 6})
any_arg()
