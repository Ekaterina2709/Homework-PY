# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
inp = 'aaaajdjjjjjdkkkeiiidhhheyyyy5555'
print('Исходная срока:',inp)
res = ''
count = 0
while True:
    for i in range(len(inp)):
        if inp[0] == inp[i]:
            count += 1
        else:
            break
    temp = count
    while temp > 0:
        res += f'{9 if temp > 9 else temp}{inp[0]}'
        temp -= 9
    inp = inp[count:]
    count = 0
    if len(inp) == 0:
        break
print(f'Сжатая строка: {res}')
