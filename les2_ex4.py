#Напишите программу, которая принимает на вход N, и координаты двух точек и находит расстояние между ними в N-мерном пространстве.
import random
import math


def get_number():
    try:
        a = int(input('Enter a number\n'))
        if a < 1:
            print('Enter a valid number')
        else:
            return a
    except:
        print('Enter a valid number')


def fill_coordinates(dims):
    crd = []
    for i in range(d):
        crd.append(random.randint(-100, 100))
    return crd


def count_distance(dot_a, dot_b, dimens):
    sum = 0
    for i in range(dimens):
        sqr = (dot_b[i] - dot_a[i]) ** 2
        sum += sqr
    distance = math.sqrt(sum)
    return distance


do = True
while do:
    d = get_number()
    A = fill_coordinates(d)
    print(A)
    B = fill_coordinates(d)
    print(B)
    dist = count_distance(A, B, d)
    print(dist)
    print("Again? Press 'N' to exit, press any other key to continue")
    want = input()
    if want == 'N' or want == 'n':
        do = False
