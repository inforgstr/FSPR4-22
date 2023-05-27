import time
import itertools


# def fibbonnaci_generator(n):
#     fib1 = 0
#     fib2 = 1

#     for _ in range(1, n):
#         if _ in (1, 2):
#             yield 1
#         else:
#             c = fib1 + fib2
#             yield c
#             fib1 = fib2
#             fib2 = c


# start = time.perf_counter()
# print(list(fibbonnaci_generator(1000)), f"{time.perf_counter()-start:8f} ms")


# def factorial_generator(n):
#     term = 1

#     for _ in range(2, n+1):
#         c = term * _
#         yield c
#         term = c


# fact = factorial_generator(10)


