# Дан список чисел.
# Создайте список, в который попадают числа, описывающие максимальную возрастающую последовательность.
# Порядок элементов менять нельзя.
#
#     *Пример:*
#

#     [1, 5, 2, 3, 4, 6, 1, 7] =>  [1, 7]
#     [1, 2, 8, 12, 3, 4,  1, 7] =>  [1, 4]


our_list = [1, 2, 8, 12, 3, 4,  1, 7, 13]

print(our_list)
count = 0
help_list = []
for i in range(len(our_list)):
    if our_list[i] + 1 in our_list:
        if our_list[i] not in help_list:
            help_list.append(our_list[i])
            help_list.append(our_list[i]+1)
help_list.sort()
print(help_list)

