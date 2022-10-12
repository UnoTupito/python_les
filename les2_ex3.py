#Напишите программу, в которой пользователь будет задавать две строки, а программа - определять количество вхождений одной строки в другой.


def search_parts(str1, str2):
    counter = 0
    for i in range(0, len(str1) - len(str2) + 1):
        helper = str1[i: i + len(str2)]
        if str2 == helper:
            counter = counter + 1
    return counter

do = True
while do:
    st1 = input('First string: ')
    st2 = input('Second string: ')

    res = search_parts(st1, st2)
    print(res)
    print("Again? Press 'N' to exit, press any other key to continue")
    want = input()
    if want == 'N' or want == 'n':
        do = 0