def n_nested(lst, nums=0):
    for var in lst:
        if isinstance(var, list):
            nums += 1
            return n_nested(var, nums)
    return nums

print(n_nested([2, [2, 3, [[[[[[[[5]]]]]]]]]]))
