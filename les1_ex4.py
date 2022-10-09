operations = ['+', '-', '/', '*', 'mod', 'pow', 'div']


def valid_number (num):
    if num == 0:
        print('Division by zero!')
    else:
        return True


def get_number():
    try:
        num = float(input())
        return num
    except:
        print('Enter only one number')


def get_operation():
    try:
        op = input()
        if op in operations:
            return op
        else:
            print('Enter a valid operation')
            return None
    except:
        print('Enter a valid operation')


agree = 1
while agree:
    num1 = None
    num2 = None
    operation = None

    while num1 is None:
        print('First number:')
        num1 = get_number()
    while num2 is None:
        print('Second number:')
        num2 = get_number()
    while operation is None:
        print('Choose an operation')
        operation = get_operation()

    if operation == '+':
        print(num1 + num2)
    elif operation == '-':
        print(num1 - num2)
    elif operation == '*':
        print(num1 * num2)
    elif operation == '/':
        if valid_number(num2):
            print(num1 / num2)
    elif operation == 'mod':
        if valid_number(num2):
            print(num1 % num2)
    elif operation == 'pow':
        print(num1 ** num2)
    else:
        if valid_number(num2):
            print(num1 // num2)

    print("Again? Press 'N' to exit, press any other key to continue")
    answer = input()
    if answer == 'N' or answer == 'n':
        agree = 0
