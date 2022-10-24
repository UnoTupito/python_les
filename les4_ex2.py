# задача 2 . Задайте последовательность чисел.
# Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.
import random


def list_creation():
    new_list = []
    amount = random.randint(1, 15)
    for i in range(amount):
        new_list.append(random.randint(1, amount))
    return new_list


def list_clean(list_to_check):
    new_list = []
    for i in list_to_check:
        if i not in new_list:
            new_list.append(i)
    return new_list


do = True
while do:
    working_list = list_creation()
    print(working_list)
    checked_list = list_clean(working_list)
    print(checked_list)
    print("Again? Press 'N' to exit, press any other key to continue")
    want = input()
    if want == 'N' or want == 'n':
        do = False
