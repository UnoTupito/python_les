#Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z .
# Но теперь количество предикатов не три, а генерируется случайным образом от 5 до 25,
# проверяем это утверждение 100 раз,
# с помощью модуля time выводим на экран , сколько времени отработала программа.
import random
import time


def create_preds(num_of_preds):
    preds = {}
    options = [True, False]
    for i in range(num_of_preds):
        preds[i] = random.choice(options)
    return preds


def check_left(dic):
    helper = True
    for i in range(amount_of_pred):
        helper = (helper and dic[i])
    res_left = not helper
    return res_left


def check_right(dic):
    res_right = True
    for i in range(amount_of_pred):
        res_right = res_right or (not dic[i])
    return res_right


amount_of_pred = random.randint(5, 25)
print(amount_of_pred)

time_start = time.time()
tries = 100
for i in range(tries):

    predicates = create_preds(amount_of_pred)

    #print(predicates)

    left_result = check_left(predicates)
    right_result = check_right(predicates)

    answer = (left_result == right_result)
    print(answer)

time_end = time.time()
time_working = time_end - time_start
print(f'The program was working {time_working} seconds')


