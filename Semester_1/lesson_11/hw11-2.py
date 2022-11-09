numbers = [2, 3, 4, 5, 6, 7]
n = []
s = []
for i in numbers:
    n.append(i) if i % 2 == 0 else s.append(i)
    # if i % 2 == 0:
    #     n.append(i)
    # else:
    #     s.append(i)
print(f'Чётные числа - {tuple(n)}')
print(f'Нечётные числа - {tuple(s)}')