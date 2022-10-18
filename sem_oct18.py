
import json

BD=[12345, True, "яблоко", {"Миша": [898981646, 464654654]}]


def load():
            # загрузить из json
            fname='BD.json' #открываем файл
            with open(fname, 'r', encoding='utf-8') as fh:  # открываем файл на чтение
                BD_local = json.load(fh)  # загружаем из файла данные в словарь data
            print('БД успещно загружена')
            return BD_local

def save():
            # сохранить в json
            with open('BD.json', 'w', encoding='utf-8') as fh:  # открываем файл на запись
                fh.write(json.dumps(BD, ensure_ascii=False))  # преобразовываем словарь data в unicode-строку и записываем в файл
            print('БД успещно сохранена')

#save()


BDnew = load ()
print(BDnew)
fib = [0, 1]
n = int(input(' Введите число: '))
fibn = [0, 1]
for i in range(2, n + 1):
    next = fib[i-1] + fib[i-2]
    if i % 2 == 0:
        fibn.append(-next)
    else:
        fibn.append(next)
    fib.append(next)
print(fib)
print(fibn)
print(fibn[1:][::-1] + fib)


def lcm(a, b):
    for i in range(max(a, b), a * b + 1):
        if i % a == 0 and i % b == 0:
            return i


def main():
    try:
        a = int(input('Input number A: '))
        b = int(input('Input number B: '))
    except ValueError as ex:
        print('Input natural number!')
        exit(ex)

    print(f'LCM({a}, {b}) = {lcm(a, b)}')
if __name__ == '__main__':
    main()


a = int(input('Введите число а '))
b = int(input('Введите число b '))
c = int(input('Введите число c '))
D = b**2 - 4*a*c
if D > 0:
    print(f'Имеет два решения {(-b + D**0.5) / 2*a} и {(-b - D**0.5) / 2*a}')
elif D < 0:
    print('Нет решений')
else:
    print(f'есть одно решение  {-b / 2 * a}')

