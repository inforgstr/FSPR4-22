def factorial(number):
    m = 1
    for i in range(1, number + 1):
        m *= i
    return m


print(factorial(5))
