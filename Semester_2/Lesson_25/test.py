lst = [2, 1, 10, 9]

for x in range(len(lst)):
    if x < len(lst) - 1:
        if lst[x] > lst[x+1]:
            lst[x] = lst[x+1]
            lst[x+1] = lst[x]
    
print(lst)
