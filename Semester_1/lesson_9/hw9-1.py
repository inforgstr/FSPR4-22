for val in [1, 2, 3, 4, 5, [3, 4, 6, 43], (3, 4, 34, 345)]:
    if isinstance(val, (list, set, tuple)):
        for i in val:
            print(i)
    else:
        print(val)
