import random

list_original = []
list_result = []
list_help = []


def get_info():
    try:
        num = int(input())
        return num
    except:
        print('Enter only one number')


def fill_list(lines, rows):
    inner_list = []
    for i in range(lines):
        inner_list.append([])
        for j in range(rows):
            inner_list[i].append(random.randint(0, 100))
    return inner_list


def print_list(printing_list):
    for i in range(line):
        for j in range(row):
            print(printing_list[i][j], end=' ')
        print('')


def put_in_one_list(big_list):
    long_list = []
    for i in range(line):
        for j in range(row):
            long_list.append(big_list[i][j])
    return long_list


def sort_list(unsorted):
    for i in range(0, len(unsorted) - 1):
        for j in range(len(unsorted) - 1):
            if unsorted[j] > unsorted[j + 1]:
                helper = unsorted[j]
                unsorted[j] = unsorted[j + 1]
                unsorted[j + 1] = helper
    return unsorted


def break_list(list_to_break):
    counter = 0
    broken_list = []
    for i in range(line):
        broken_list.append([])
        for j in range(row):
            broken_list[i].append(list_to_break[counter])
            counter += 1
    return broken_list


print('number of lines')
line = get_info()
print('number of rows')
row = get_info()


list_original = fill_list(line, row)
print(list_original)

print_list(list_original)

list_help = put_in_one_list(list_original)
print(list_help)

list_help = sort_list(list_help)
print(list_help)

list_result = break_list(list_help)
print(list_result)

print_list(list_result)






