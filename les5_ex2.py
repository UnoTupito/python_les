# задача 2. Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.


def compress_str(g_str):
    com_str = ''
    count_a = 1
    for i in range(len(g_str) - 1):
        a = g_str[i]
        if g_str[i] == g_str[i + 1]:
            count_a += 1
        else:
            com_str = com_str + a + str(count_a)
            count_a = 1
        if i == len(g_str) - 2 and g_str[i] == g_str[i + 1]:
            com_str = com_str + a + str(count_a)
        elif i == len(g_str) - 2 and g_str[i] != g_str[i + 1]:
            com_str = com_str + g_str[i + 1] + '1'
    return com_str


given_str = input('Enter your text to compress:\n')
compressed_str = compress_str(given_str)
print(compressed_str)


# AAAAAAFDDCCCCCCCAEEEEEEEEEEEEEEEEE