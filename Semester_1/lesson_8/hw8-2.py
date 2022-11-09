xp = int(input('Введите xp вашего героя: '))
damage = int(input('Введите урон вашего героя: '))
mp = int(input('Введите mp вашего героя: '))

if xp <= 100 and damage <=10 and mp <= 50:
    print('Уровень героя - 1')
elif xp <= 300 and damage <=20 and mp <= 100:
    print('Уровень героя - 10')
elif xp <= 500 and damage <=100 and mp <= 200:
    print('Уровень героя - 15')
else:
    print('Вы герой!')