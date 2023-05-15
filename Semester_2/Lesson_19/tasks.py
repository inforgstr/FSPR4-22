def sum_dig_pow(a, b): # range(a, b + 1) will be studied by the function
    result = []
    counter = 1
    
    for x in range(a, b+1):
        num = 0

        for digit in str(x):
            num += int(digit)**counter

            counter += 1
        if num==x:
            result.append(num)

        counter = 1
    return result

print(sum_dig_pow(1, 100))
