c = []
a = [1, 2, 'helloes', 3, 4, 5, 6, 'hello', 7]
for ab in a:
    if isinstance(ab, (int, float)):
        c.append(ab*4)
print(c)