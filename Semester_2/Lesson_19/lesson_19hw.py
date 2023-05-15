"""
HW:
    1. Решить два задачи из кодварса на 6 кью и одну на 5 кью.
    2. Узнать, сколько вложенных списков, есть внутри данного списка: [2, [2 , 3, [[[[[[[[5]]]]]]]]]].
"""


"""ex: 1"""

# Problem for 5kyu - problem name `Human Readable Time`:
# https://www.codewars.com/kata/52685f7382004e774f0001f7/train/python

def make_readable(seconds):
    hours = seconds//3600
    minutes = (seconds-hours*3600)//60
    sec = seconds - (hours*3600+minutes*60)

    lst = [f"0{x}" if len(str(x))==1 else str(x) for x in (hours, minutes, sec)]
    return ":".join(lst)



# Problem for 6kyu - problem name `+1 Array`:
# https://www.codewars.com/kata/5514e5b77e6b2f38e0000ca9/train/python


def up_array(arr: list[int]) -> list[int]:
    if not arr:
        return None
    hint = 0

    i = len(arr) - 1
    while i != -1:
        if len(str(arr[i])) == 2 or "-" in str(arr[i]):
            return None
        else:
            if arr[i] + 1 == 10:
                if i == arr.index(arr[0]):
                    if len(arr[i:]) == hint + 1:
                        arr[i] = 0
                        arr.insert(0, 1)
                    else:
                        arr[0] = arr[i]

                elif i != arr.index(arr[0]) and len(arr[i:]) == hint + 1:
                    arr[i] = 0
                    hint += 1
            else:
                if len(arr[i:]) == hint + 1:
                    arr[i] += 1
        i -= 1
    return arr


# Problem for 6kyu - problem name `Take a Number And Sum Its Digits Raised To The Consecutive Powers And ....¡Eureka!!`
# https://www.codewars.com/kata/5626b561280a42ecc50000d1/train/python


def sum_dig_pow(a, b):
    """
    range(a, b + 1) will be studied by the function
    """
    result = []
    counter = 1

    for x in range(a, b + 1):
        num = 0

        for digit in str(x):
            num += int(digit) ** counter

            counter += 1
        if num == x:
            result.append(num)

        counter = 1
    return result


"""ex: 2"""
# With for loop
lst = [2, [2, 3, [[[[[[[[5]]]]]]]]]]
counter = 0
quantity = 0

for i in range(13):
    if isinstance(lst[counter], list):
        lst = lst[counter]
        counter = 0

        quantity += 1
    else:
        counter += 1

# print(quantity)


# With recursive
def n_nested(lst: list) -> int:
    """
    Args:
        lst (list): iterable

    Returns:
        int: Number of nested lists
    """
    n = 0

    for value in lst:
        if isinstance(value, list):
            n += 1
            return n_nested(value)
        return 1
    print(value, n)
    


print(n_nested([2, [2, 3, [[[[[[[[5]]]]]]]]]]))
