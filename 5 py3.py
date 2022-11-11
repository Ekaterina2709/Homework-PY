# Создайте программу для игры в "Крестики-нолики"

import random
a1 = a2 = a3 = b1 = b2 = b3 = c1 = c2 = c3 = ' '
x = 'X'
o = 'O'
count = 0


def board():
    print('   1   2   3 ')
    print('A', a1, '  |', a2, '|', a3)
    print('   ---|---|---')
    print('B', b1, '  |', b2, '|', b3)
    print('   ---|---|---')
    print('C', c1, '  |', c2, '|', c3)


def inp(id):
    global a1, a2, a3, b1, b2, b3, c1, c2, c3, count
    count += 1
    while True:
        ad = input('Укажите адрес ячейки (а1,а2,b3 итд): ')
        if ad == 'a1' and a1 == ' ':
            a1 = id
            break
        elif ad == 'a2' and a2 == ' ':
            a2 = id
            break
        elif ad == 'a3' and a3 == ' ':
            a3 = id
            break
        elif ad == 'b1' and b1 == ' ':
            b1 = id
            break
        elif ad == 'b2' and b2 == ' ':
            b2 = id
            break
        elif ad == 'b3' and b3 == ' ':
            b3 = id
            break
        elif ad == 'c1' and c1 == ' ':
            c1 = id
            break
        elif ad == 'c2' and c2 == ' ':
            c2 = id
            break
        elif ad == 'c3' and c3 == ' ':
            c3 = id
            break
        else:
            print('Ошибка ввода. Повторите ввод')


def ig():
    if (a1 == a2 == a3 == 'X' or b1 == b2 == b3 == 'X' or c1 == c2 == c3 == 'X' or a1 == b1 == c1 == 'X' or a2 == b2 == c2 == 'X' or a3 == b3 == c3 == 'X' or a1 == b2 == c3 == 'X' or a3 == b2 == c1 == 'X'):
        print('Выйграли крестики')
        exit()
    if (a1 == a2 == a3 == 'O' or b1 == b2 == b3 == 'O' or c1 == c2 == c3 == 'O' or a1 == b1 == c1 == 'O' or a2 == b2 == c2 == 'O' or a3 == b3 == c3 == 'O' or a1 == b2 == c3 == 'O' or a3 == b2 == c1 == 'O'):
        print('Выйграли нолики')
        exit()
    if count == 9:
        print('Ничья')
        exit()


board()
print('Первые играют:', player := random.choice(
    ['крестики', 'нолики']), end="\n")
if player == 'нолики':
    inp(o)
    board()
while True:
    inp(x)
    board()
    if count > 4:
        ig()
    inp(o)
    board()
    if count > 4:
        ig()
