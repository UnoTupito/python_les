# задача 1. Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.


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
        for i in range(2, num+1):
            if number % i == 0:
                if is_prime(i):
                    mult_list.append(i)
                    number = number // i
                    break
    return mult_list


num = int(input('Enter a number'))
mults = look_for_num(num)
print(mults)

