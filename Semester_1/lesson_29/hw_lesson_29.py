def num_of_open_lockers(n):
    res = [0 for i in range(n)]

    for number in range(n):
        for j in range(2, n+1):
            if number % j == j-1:
                res[number] = 1 if res[number] == 0 else 0

    return res.count(0)

# or 
def num_of_open_lockers(n):
    return int(n**(1/2))

print(num_of_open_lockers(324242478))