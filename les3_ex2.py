def fill_list():
    add = True
    filled_list = []
    while add:
        print("Add a number to your list. Press 'N' to exit")
        add = input()
        if add == 'N' or add == 'n':
            add = False
        else:
            filled_list.append(int(add))
    return filled_list


def count_mult(given_list):
    result_list = []
    for i in range(1, len(given_list) // 2 + 1):
        result_list.append(given_list[i-1]*given_list[-i])
    if len(given_list) % 2 != 0:
        result_list.append(given_list[len(given_list)//2]**2)
    return result_list


working_list = []

try:
    working_list = fill_list()
except:
    print('Only numbers')

if not working_list:
    print('No numbers in the list')
else:
    print(f'Your list is the following:\n{working_list}')
    needed_list = count_mult(working_list)
    print(f'The multiplication of the pairs is:\n{needed_list} ')