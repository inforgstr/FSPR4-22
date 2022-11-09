faranheits = [20, 19, 24, 45, 140]
i = 0
while i < len(faranheits):
    celsius = ((faranheits[i]) - 32) * 5 / 9
    if celsius >= 50:
        print(f"Слишком горячо: {celsius}")
        break
    elif celsius <= 5:
        print(f"Жить можно: {celsius}")
    i += 1