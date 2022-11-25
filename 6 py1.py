# Напишите программу вычисления арифметического выражения 
# заданного строкой. Используйте операции +,-,/,*. приоритет операций стандартный.

# Пример:
# 2+2 => 4;
# 1+2*3 => 7;
# 1-2*3 => -5;

# Добавьте возможность использования скобок, 
# меняющих приоритет операций.
# Пример:
# 1+2*3 => 7;
# (1+2)*3 => 9;


import re


res = []
arifm = input('Введите арифметическое выражение:\n ')
example = re.split('(\W)', arifm)  # получаем список элементов вместо строки
             
i = 0
while i < len(example): 
    if example[i] == '-':
        res.append(0 - float(example[i + 1])) 
        i += 2
    elif example[i] == '+':
        res.append(float(example[i + 1])) 
        i += 2
    else:
        res.append(example[i]) 
        i += 1

for n in range(len(res)):  
    if res[n] == '/':
        res[n + 1] = (float(res[n - 1]) / float(res[n + 1]))  
        res[n - 1] = res[n] = 0  

res = [x for x in res if x != 0]  

for j in range(len(res)):  
    if res[j] == '*':
        res[j + 1] = (float(res[j - 1]) * float(res[j + 1]))
        res[j - 1] = res[j] = 0

res = [x for x in res if x != ''] 
print("Ответ")
print(sum(map(float, res))) 

Я написала кусок программы которая будет раскрывать скобки в выражении напимер при выражении 25+(5*(1+2))
программа выдает список во внутренних скобках [1,+,2]. Посчить скобку можно с помощью верхней части программы.
Затем получившееся число нужно вставить в исходный список вместо (1+2). Я всю логику понимаю но соединить у меня не получается. 
Я сижу на этим уже больше недели. Прошу у вас помощи.

# new = [x for x in example if x != '']
# prom_res =[]
# y = 0
# x = 0
# for x in range(len(new)): 
#     if new[x] == '(':    # ищем последнюю откр-ся скобку
#         num = x          #узнаем ее индекс
# for y in range(num+1):
#     if y<=num:
#         res = new[y]=0   # все елементы до скобки меняем на 0 

# for k in range(len(new)): 
#     if new[k] == ')':    # ищем первую закр-ся скобку
#         num2 = k
#         break      
# for e in range(len(new)):
#         if e>=num2:
#             res = new[e]=0  # все елементы после скобки меняем на 0
# prom_res = [n for n in new if n != 0]  # удаляем нули из списка получаем первую скобку для расчета                                        
# print(example)
# print(prom_res)
# print(example_new)
