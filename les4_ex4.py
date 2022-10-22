# Найдите корни квадратного уравнения, уравнение вводит через строку пользователь.
# например, 6 * x^2 + 5 * x + 6 = 0 . Само собой, уравнение может и не иметь решения.
# Предусмотреть все варианты, сделать обработку исключений.


def equation_trim(equation_str):
    equation_str = equation_str.replace(' ', '')  # убрали пробелы (пользователь, конечно, дурак, но всё-таки расчитываю, что он вводит только обычные пробелы)
    equation_str = equation_str.replace('**', '^')  # если пользователь догадался показать степень двумя звёздочками, исправили
    equation_str = equation_str.replace('*', '')  # убрали звёздочки, если пользователь показывал ими умножение.
    equation_str = equation_str[:-2]  # уравнение должно заканчиваться на =0 - мы это убрали
    return equation_str


def find_equation_parts(koef_list_all):
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


def find_a(koef_list_parts):
    A = 0
    for i in range(len(koef_list_parts)):  # ищем А - там должен быть Х в степени 2
        if 'x^2' in koef_list_parts[i]:
            if len(koef_list_parts[i]) == 3:  # если 3 символа, то есть только Х в степени 2
                A = 1
                break
            elif len(koef_list_parts[i]) == 4:
                if koef_list_parts[i][0] == '-':  # если 4 символа, первым может оказаться минус
                    A = -1
                    break
                else:
                    A = int(koef_list_parts[i][:-3])  # убираем Х в степени два и остаётся коэффициент
                    koef_list_parts.remove(koef_list_parts[i])
                    break
            else:
                A = int(koef_list_parts[i][:-3])  # убираем Х в степени два и остаётся коэффициент
                koef_list_parts.remove(koef_list_parts[i])
                break
    return A


def find_b(koef_list_parts):
    B = 0
    for i in range(len(koef_list_parts)):
        if 'x' in koef_list_parts[i] and '^' not in koef_list_parts[i]:  # ищем В - у него есть Х, но не будет степени
            if len(koef_list_parts[i]) == 1:
                B = 1
                break
            elif len(koef_list_parts[i]) == 2:  # если 2 символа, то первым может быть минус
                if koef_list_parts[i][0] == '-':
                    B = -1
                    break
            else:
                B = int(koef_list_parts[i].replace('x', ''))
    return B


def find_c(koef_list_parts):
    C = 0
    for i in range(len(koef_list_parts)):  # ищем С - у него нет своего Х
        if 'x' not in koef_list_parts[i]:
            C = int(koef_list_parts[i])
            koef_list_parts.remove(koef_list_parts[i])
    return C


def find_roots(a, b, c):
    D = b ** 2 - 4 * a * c
    if D > 0:
        print(f'Имеет два решения {(-b + D ** 0.5) / (2 * a)} и {(-b - D ** 0.5) / (2 * a)}')
    elif D < 0:
        print('Нет решений')
    else:
        print(f'есть одно решение  {-b / 2 * a}')

do = True
while do:
    equ_str = None
    while equ_str is None:
        equ_str = input('Enter your equation\n')
        if '**2' not in equ_str and '^2' not in equ_str:
            print('It is not a quadratic equation. Try again.')
            equ_str = None
    try:
        equ_str = equation_trim(equ_str)
        kf_list_all = equ_str.split('+')
        kf_list_parts = find_equation_parts(kf_list_all)
        A = find_a(kf_list_parts)
        B = find_b(kf_list_parts)
        C = find_c(kf_list_parts)
        print(f'A is {A}, B is {B}, C is {C}')
        find_roots(A, B, C)
    except:
        print('It seems it not a reduced quadratic equation. Try again.')  # будет корректно ругаться, если уравнение квадратное, но не приведённое
    print("Again? Press 'N' to exit, press any other key to continue")
    want = input()
    if want == 'N' or want == 'n':
        do = False

#9*x^2 -1 = 0
#2x^2-5x+2 = 0
#x^2-5x=0
#-x**2-3x-4-2=0
#x-5xx=0