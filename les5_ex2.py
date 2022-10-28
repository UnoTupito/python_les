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


with open('les5_ex2_read.txt', 'r') as data_to_compress:
    given_str = data_to_compress.read()
compressed_str = compress_str(given_str)
print(compressed_str)
with open('les5_ex2_write.txt', 'w') as data_compressed:
    data_compressed.write(compressed_str)


# AAAAAAFDDCCCCCCCAEEEEEEEEEEEEEEEEE