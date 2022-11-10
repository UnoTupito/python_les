# task = input('Введите пример')
task = '11+2*3-1'
task.replace(' ', '')

if '*' in task:
    a = task.index("*")
    answer = int(task[a-1]) * int(task[a+1])
    task = task[0:a-1] + str(answer) + task[a+2:]
    print(task)

if '/' in task:
    a = task.index("/")
    answer = int(task[a-1]) / int(task[a+1])
    task = task[0:a-1] + str(answer) + task[a+2:]
    print(task)

if '+' in task:
    parts = task.split('+')
    print(parts)
    for i in parts:
        if '-' in i:
            def_parts = i.split('-')
            print(def_parts)
            dif = 0
            for j in def_parts:
                dif -= int(j)
            i = dif
    print(dif)
    # sum_parts = 0
    # for i in parts:
    #     sum_parts += int(i)
    # print(sum_parts)
    # a = task.index('+')
    # answer = int(task[:a]) + int(task[a+1:])
    # print(answer)
