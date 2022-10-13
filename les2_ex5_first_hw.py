#для подготовки разобралась с простой версией

x = [True, False]
y = [True, False]
z = [True, False]

for i in x:
    for j in y:
        for l in z:
            answer = (not(x and y and z) == (not x) or (not y) or (not z))
            print(answer)