with open("dataset_3363_4 (1).txt", "r") as file:
    words = file.read().lower().split()


overall = []
for word in words:
    res = word.split(";")
    num = 0
    i = 1
    overall.append(res)
    for char in res:
        if char.isdigit():
            num += int(char)
    print(num / 3)
    res = []
    while i < len(word) and word[i].isdigit():
        res.append(word[i])
        i += 1
i1 = i2 = i3 = 0
for num in overall:
    i1 += int(num[1])
    i2 += int(num[2])
    i3 += int(num[3])

print(i1/len(overall), i2/len(overall), i3/len(overall))
