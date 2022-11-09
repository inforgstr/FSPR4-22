def fib_numbers(n):
    fi1 = 1
    fi2 = 1
    for i in range(2, n):
        f = fi1 + fi2
        fi1 = fi2
        fi2 = f
    return f

numbers = int(input('Input number: '))
print(fib_numbers(numbers))