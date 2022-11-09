# def factorial(number):
#     '''Returns factorial of the number'''
#     for i in range(1, number):
#         fac = number * i
#         number = fac
#     return fac

# print(factorial(8))   0 1 1 2 3 + 5 = 8 13 ...

def f(n):
    if n == 0:
        return 0
    return f(n+1)
print(f(55))