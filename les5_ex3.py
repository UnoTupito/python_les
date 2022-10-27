# Напишите программу, удаляющую из текста все слова, содержащие "абв". Функции FIND и COUNT юзать нельзя.


def find_and_del(g_str):
    n_str = ''
    indices = []

    for i in range(len(g_str) - len(symbols_to_delete) + 1):
        if g_str[i:i + len(symbols_to_delete)] == symbols_to_delete:
            indices.append(i)
    left_ind = 0
    for i in indices:
        n_str = n_str + g_str[left_ind:i]
        left_ind = i + len(symbols_to_delete)
    n_str = n_str + g_str[left_ind:]
    return n_str


given_str = input('Enter your text:\n')
symbols_to_delete = input('Enter symbols to find and delete: ')
new_str = find_and_del(given_str)
print('Your new text:')
print(new_str)
