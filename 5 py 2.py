# Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока 
# делая ход друг после друга. Первый ход определяется жеребьёвкой. 
# За один ход можно забрать не более чем 28 конфет. Все конфеты 
# оппонента достаются сделавшему последний ход. Сколько конфет нужно 
# взять первому игроку, чтобы забрать все конфеты у своего конкурента?
# a) Добавьте игру против бота
# b) Подумайте как наделить бота ""интеллектом""

import random
print('''Игра:На столе лежит 2021 конфета. Играют два игрока 
делая ход друг после друга. Первый ход определяется жеребьёвкой. 
За один ход можно забрать не более чем 28 конфет. Все конфеты 
оппонента достаются сделавшему последний ход''')
n = int(input('Введите число игроков (1-если играть с компьютером, 2 - если с оппонентом)- '))
candy = 100
max = 28
min = 1
count = 0
player = random.randint(1, 2)
while candy > 0:
    if player == 1:
        player = 2
    else:
        player = 1
    count += 1
    if n == 1 and player == 2:
        print(count, 'ход: Всего', candy, 'конфет. Компьютер ', end='')
        if candy <= max:
            c = candy
        else:
            c = random.randint(1, 28)
        print('забирает', c)
        candy -= c
    else:
        print(count, 'ход: Всего', candy, 'конфет. Игрок', player, end='')
        c = int(input(' забирает:'))
        if c < min or c > max:
            c = 0
            print('\nНельзя брать больше 28 конфет или меньше одной конфеты Игрок',
                  player, 'Возьмите еще раз')
            count -= 1
            if player == 1:
                player = 2
            else:
                player = 1
        elif c > candy and candy < max:
            c = 0
            print('\nСтолько конфет нет. Игрок', player,
                  'Возьмите другое колличество конфет из оставшихся', candy)
            count -= 1
            if player == 1:
                player = 2
            else:
                player = 1
        candy -= c
if n == 1 and player == 2:
    print('Победа! Компьютер победил за', count,
          'ходов и забирает все конфеты!')
else:
    print('Победа! Игрок', player, 'победил за',
          count, 'ходов и забирает все конфеты!')