dict_a = [{'name': 'python', 'points': 10}, {'name': 'java', 'points': 8}]

dict_a = [5,8,6,1,0,99]


res = list(filter(lambda x : x > 5, dict_a)) # Вернет: [{'name': 'python', 'points': 10}]

if not res:
    print('список пуст')
else:
    print(res)


