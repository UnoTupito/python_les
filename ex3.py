
def get_number():
    try:
        num = float(input())
        if num == 0:
            print('Your numbers cannot be zero')
        else:
            return num
    except:
        print('Enter only one number')


def check_quarter(x, y):
    if x > 0 and y > 0:
        print('The dot is in the FIRST quarter')
    elif x > 0 and y < 0:
        print('The dot is in the SECOND quarter')
    elif x < 0 and y < 0:
        print('The dot is in the THIRD quarter')
    else:
        print('The dot is in the FORTH quarter')


agree = 1
while agree:
    print('Enter your numbers')
    x = None
    y = None
    while x is None:
        print('X = ')
        x = get_number()
    while y is None:
        print('Y = ')
        y = get_number()
    print(x, y)

    check_quarter(x, y)

    print("Again? Press 'N' to exit, press any other key to continue")
    answer = input()
    if answer == 'N' or answer == 'n':
        agree = 0

