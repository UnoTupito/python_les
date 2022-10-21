# Задана натуральная степень k.
# Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена
# и записать в файл многочлен степени k.
#
# *Пример:*
# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0
import random


def create_polyn(kf):
    polyn = ''
    for i in range(kf, 0, -1):
        a = random.randint(0, 10)
        if a == 0:
            pass
        elif a == 1:
            polyn = polyn + 'x^' + str(i)
        else:
            polyn = polyn + str(a) + 'x^' + str(i)
        if i != 1:
            if polyn[-1] == '+':
                pass
            else:
                polyn = polyn + '+'
    if polyn != '':
        polyn = polyn + '=0'
    return polyn


do = True
while do:
    k = int(input('Enter k\n'))
    res = create_polyn(k)
    print(res)
    print("Again? Press 'N' to exit, press any other key to continue")
    want = input()
    if want == 'N' or want == 'n':
        do = False