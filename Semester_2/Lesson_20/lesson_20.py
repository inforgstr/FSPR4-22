# # numbers = [i for i in range(10)]
# # numbers_2 = [i for i in range(10, 15)]
# # numbers_3 = [i for i in range(20, 30)]


# # print(list(map(lambda x, y, z: x*y*z, numbers, numbers_2, numbers_3)))
# # ([1, 2], [1, 2])  [1, 2]
# import time

# def map(func, *iterable):
#     start = time.perf_counter()
#     result = []
#     lst = []

#     min_length = sorted(iterable, key=lambda x: len(x))[0]
    
#     for iter in iterable:
#         if not(isinstance(iter, int) or isinstance(iter, float) or isinstance(iter, bool)):
#             var = iter[:len(min_length)]
#             res = []


#         else:
#             raise TypeError
        
#     return result, lst, f"{time.perf_counter()-start:8f}"

# print(map(lambda x, y:x+1, [1, 2], [1, 3]))




# # print(list(filter(lambda x: x>=3, [1, 2, 3, 4, 5])))

# print(list(map(lambda x, y: x+1, [1, 2], [1, 3])))

# print(list(filter(lambda x: x+1==0, [1, 2, 3, 4, -1])))
