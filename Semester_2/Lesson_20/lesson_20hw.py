"""
Написать реализацию функции map и filter.
"""
# map
def map_2(func, *iterable):
    d = {}

    min_length = min([len(x) for x in iterable])

    for iter in iterable:
        for i in range(min_length):
            if i in d:
                d[i].append(iter[i])
            else:
                d[i] = [iter[i]]

    return [func(*d[variable]) for variable in d]


print(map_2(lambda x, y, z: x+y+z, [1, 2], [2, 3, 4], [10, 12, 2, 3, 4]))


# filter
def filter_2(func, iterable):
    return [variable for variable in iterable if func(variable)]


# print(filter_2(lambda x: x > 1, [1, 2, 1, 1]))
