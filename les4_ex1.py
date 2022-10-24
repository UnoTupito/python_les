# задача 1. Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.


def get_number():
    try:
        a = int(input('Enter a number\n'))
        if a < 1:
            print('Enter a valid number')
        else:
            return a
    except:
        print('Enter a valid number')


def is_prime(numb):
    if numb % 2 == 0:
        return numb == 2
    a = 3
    while numb % a != 0:
        a += 1
    return a == numb


def look_for_num(number):
    mult_list = []
    while number > 1:
        for i in range(2, num + 1):
            if number % i == 0:
                if is_prime(i):
                    mult_list.append(i)
                    number = number // i
                    break
    return mult_list



do = True
while do:
    num = None
    while num is None:
        num = get_number()
    mults = look_for_num(num)
    print(mults)
    print("Again? Press 'N' to exit, press any other key to continue")
    want = input()
    if want == 'N' or want == 'n':

        do = False
