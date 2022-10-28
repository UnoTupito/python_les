# Дан список чисел.
# Создайте список, в который попадают числа, описывающие максимальную возрастающую последовательность.
# Порядок элементов менять нельзя.


given_list = [1, 5, 3, 4, 2, 1, 7, 8, 15, 1]


def find_sequence(g_list):
    lists = []
    small_list = []
    a = min(g_list)
    small_list.append(a)
    while a <= max(g_list):
        if a not in g_list:
            a += 1
            pass
        else:
            if a not in small_list:
                small_list.append(a)
            if a + 1 in g_list:
                small_list.append((a+1))
                a += 1
            else:
                lists.append(small_list)
                small_list = []
                a += 1
    print('The sequences in the list are the following:')
    print(lists)
    l = 0
    for i in range(len(lists)-1):
        if len(lists[l]) < len(lists[i+1]):
            l = i + 1
    res_list = [min(lists[l]), max(lists[l])]
    return res_list


print('The list we work with:')
print(given_list)
find_seq = []
result_list = find_sequence(given_list)
print('The least and the biggest numbers in the longest sequence are:')
print(result_list)
