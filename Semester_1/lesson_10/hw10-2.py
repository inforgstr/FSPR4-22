f = [20, 19, 24, 45]
for fs in f:
    s = (fs - 32) * 5/9
    if s > 50:
        print(f'{s} - слишком горячо')
        break
    elif s < 5:
        print(f'{s} - жить можно')