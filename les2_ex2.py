# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.


def get_number():
    try:
        a = int(input('Enter a number\n'))
        if a < 1:
            print('Enter a valid number')
        else:
            return a
    except:
        print('Enter a valid number')


def num_fuc(b):
    answer = 1
    answer_list = []
    for i in range(1, b+1):
        answer = answer * i
        answer_list.append(answer)

    return answer_list


do = True

while do:
    num = None
    while num is None:
        num = get_number()

    res = num_fuc(num)
    print(res)
    print("Again? Press 'N' to exit, press any other key to continue")
    want = input()
    if want == 'N' or want == 'n':
        do = 0


