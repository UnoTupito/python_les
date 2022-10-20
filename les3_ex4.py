def find_two(num):
    two = ''
    while num > 0:
        a = num % 2
        two = two + str(a)
        num = num // 2
        if num < 1:
            break
    return two


do = True
while do:
    num_ten = int(input('Enter your number:\n'))
    num_two = find_two(num_ten)
    print(f'Number {num_ten} in binary system is {num_two}')

    print("Again? Press 'N' to exit, press any other key to continue")
    answer = input()
    if answer == 'N' or answer == 'n':
        do = 0