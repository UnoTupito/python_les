# Даны два многочлена. Задача - сформировать их сумму.
# например, 5*x^3 + 2*x^2 + 6 и 7*x^2+6*x+3 , Тогда их сумма будет равна 5*x^3 + 9*x^2 + 6*x + 9


def one_style(given_str):
    given_str = given_str.replace(' ', '')
    given_str = given_str.replace('**', '^')
    given_str = given_str.replace('*', '')
    return given_str


def find_equation_parts(koef_list_all):
    koef_list_parts = []
    for i in range(len(koef_list_all)):  # азбиваем на коэффициенты, отлавливаем отрицательные
        if '-' in koef_list_all[i]:
            help_list = list(koef_list_all[i])
            for j in range(len(help_list) - 1, 0, -1):
                if help_list[j] == '-':
                    help_list.insert(j, '$')
            help_str = ''
            for l in help_list:
                help_str = help_str + l
            koef_list_all[i] = help_str
            koef_list_parts = koef_list_all[i].split('$')
        else:
            koef_list_parts.append(koef_list_all[i])
    #print(f'The parts:{koef_list_parts}')
    return koef_list_parts


str1 = '5*x^3 + 2*x^2 + 6'
str1 = one_style(str1)
list1 = find_equation_parts(str1.split('+'))
print(list1)

str2 = '7*x^2+6*x+3'
str2 = one_style(str2)
list2 = find_equation_parts(str2.split('+'))
print(list2)

res_equation = []



