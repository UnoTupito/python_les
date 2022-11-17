# Напишите программу вычисления арифметического выражения заданного строкой.
# Используйте операции +,-,/,*. приоритет операций стандартный.
# кажется, я решила очень перегруженно и сложно. врял ли эта задача пополнит золотой фонд моих кодов,
# но я тем не менее рада, что сделала её сама, хотя изначально собиралась вообще не решать из-за сложности
# программа не работает со скобками и степенями

import re


def get_mult(tsk):
    mult_pattern = r'\d+\.?\d*\*\d+\.?\d*'
    part = (re.search(mult_pattern, tsk)).group(0)
    a = float(part[:part.find('*')])
    b = float(part[part.find('*') + 1:])
    answ = str(a * b)
    tsk = tsk[0:tsk.find(part)] + answ + tsk[tsk.find(part) + len(part):]
    return tsk


def get_div(tsk):
    div_pattern = r'\d+\.?\d*\/\d+\.?\d*'
    part = (re.search(div_pattern, tsk)).group(0)
    answ = str(float(part[:part.find('/')]) / float(part[part.find('/') + 1:]))
    tsk = tsk[0:tsk.find(part)] + answ + tsk[tsk.find(part) + len(part):]
    return tsk


def get_sum(tsk):
    sum_pattern = r'\d+\.?\d*\+\d+\.?\d*'
    part = (re.search(sum_pattern, tsk)).group(0)
    answ = str(float(part[:part.find('+')]) + float(part[part.find('+') + 1:]))
    tsk = tsk[0:tsk.find(part)] + answ + tsk[tsk.find(part) + len(part):]
    return tsk


def get_dif(tsk):
    dif_pattern = r'\-?\d+\.?\d*\-\d+\.?\d*'
    part = (re.search(dif_pattern, tsk)).group(0)
    if tsk[0] == '-':
        answ = str(float(part[:part.find('-', 1)]) - float(part[part.find('-', 1) + 1:]))
    else:
        answ = str(float(part[:part.find('-')]) - float(part[part.find('-') + 1:]))
    tsk = tsk[0:tsk.find(part)] + answ + tsk[tsk.find(part) + len(part):]
    return tsk


def calc(tsk):
    float_pattern = r'^\-?\d+\.?\d*$'
    if re.match(float_pattern, tsk):
        return tsk
    elif '*' in tsk and '/' in tsk:
        if tsk.find('*') < tsk.find('/'):
            tsk = get_mult(tsk)
            tsk = calc(tsk)
            return tsk
        else:
            tsk = get_div(tsk)
            tsk = calc(tsk)
            return tsk
    elif '*' in tsk:
        tsk = get_mult(tsk)
        tsk = calc(tsk)
        return tsk
    elif '/' in tsk:
        tsk = get_div(tsk)
        tsk = calc(tsk)
        return tsk
    elif '+' in tsk and '-' in tsk:
        if tsk.find('+') < tsk.find('-'):
            tsk = get_sum(tsk)
            tsk = calc(tsk)
            return tsk
        else:
            tsk = get_dif(tsk)
            tsk = calc(tsk)
            return tsk
    elif '+' in tsk:
        tsk = get_sum(tsk)
        tsk = calc(tsk)
        return tsk
    elif '-' in tsk:
        tsk = get_dif(tsk)
        tsk = calc(tsk)
        return tsk


work = True
while work:
    task = input('Enter your problem: ')
    task = task.replace(' ', '')
    print('answer: ' + calc(task))
    print('One more? Enter N to exit.')
    a = input()
    if a == 'N' or a == 'n':
        work = False