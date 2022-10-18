#Задайте список из нескольких чисел.
# Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.

#*Пример:* - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12


def fill_list():
    add = True
    filled_list = []
    while add:
        print("Add a number to your list. Press 'N' to exit")
        a = input()
        if a == 'N' or a == 'n':
            add = False
        else:
            filled_list.append(int(a))
    return filled_list


def count_sum(working_list):
    needed_sum = 0
    for i in range(1, len(working_list)):
        if i % 2 != 0:
            needed_sum += working_list[i]
    return needed_sum


working_list = []
try:
    working_list = fill_list()
except:
    print('Only numbers')

if not working_list:
    print('No numbers in the list')
else:
    print(f'Your list is the following:\n{working_list}')
    sum = count_sum(working_list)
    print(f'The sum of numbers with odd indices is {sum}')