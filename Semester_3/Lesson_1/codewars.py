# 5kyu Calculating with Functions link: https://www.codewars.com/kata/525f3eda17c7cd9f9e000b39

SOLWERS = {
    "+": lambda a, b: a + b,
    "-": lambda a, b: a - b,
    "*": lambda a, b: a * b,
    "/": lambda a, b: a // b,
}


def zero(args=None):
    a = 0
    if args:
        operation = args[1]
        return SOLWERS.get(operation)(a, args[0])

    return a


def one(args=None):
    a = 1
    if args:
        operation = args[1]
        return SOLWERS.get(operation)(a, args[0])

    return a


def two(args=None):
    a = 2
    if args:
        operation = args[1]
        return SOLWERS.get(operation)(a, args[0])

    return a


def three(args=None):
    a = 3
    if args:
        operation = args[1]
        return SOLWERS.get(operation)(a, args[0])

    return a


def four(args=None):
    a = 4
    if args:
        operation = args[1]
        return SOLWERS.get(operation)(a, args[0])

    return a


def five(args=None):
    a = 5
    if args:
        operation = args[1]
        return SOLWERS.get(operation)(a, args[0])

    return a


def six(args=None):
    a = 6
    if args:
        operation = args[1]
        return SOLWERS.get(operation)(a, args[0])

    return a


def seven(args=None):
    a = 7
    if args:
        operation = args[1]
        return SOLWERS.get(operation)(a, args[0])

    return a


def eight(args=None):
    a = 8
    if args:
        operation = args[1]
        return SOLWERS.get(operation)(a, args[0])

    return a


def nine(args=None):
    a = 9
    if args:
        operation = args[1]
        return SOLWERS.get(operation)(a, args[0])

    return a


def plus(num):
    return num, "+"


def minus(num):
    return num, "-"


def times(num):
    return num, "*"


def divided_by(num):
    return num, "/"

# print(two(times(four())))


# 6kyu Reverse every other word in the string link: https://www.codewars.com/kata/58d76854024c72c3e20000de


def reverse_alternate(s):
    return " ".join(x[::-1] if idx % 2 else x for idx, x in enumerate(s.split()))
