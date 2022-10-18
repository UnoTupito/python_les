# Задайте список из вещественных чисел.
# Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
#*Пример:*
# [1.1, 1.2, 3.1, 5, 10.01] => 0.19


def fill_list():
    add = True
    filled_list = []
    while add:
        print("Add a number to your list. Press 'N' to exit")
        a = input()
        if a == 'N' or a == 'n':
            add = False
        else:
            filled_list.append(float(a))
    return filled_list


def find_dif(given_list):
    max_num = 0
    min_num = 0
    for i in given_list:
        b = i % 1
        if b > max_num:
            max_num = b
        if b < min_num:
            min_num = b
    return max_num - min_num


working_list = [1.1, 1.2, 3.1, 5, 10.01]
# try:
#     working_list = fill_list()
# except:
#     print('Only numbers')
print(f'Your list:\n{working_list}')
print(f'The difference between the biggest and the smallest fractional parts:\n{find_dif(working_list)}')

