do = True
while do:

    num = float(input('Enter a number'))
    sum = 0

    while num % 1 != 0: #если число делится без остатка на 1, то оно целое
        num *= 10
        #print(num)

    while num // 10 >= 0: #цикл мог бы стать бесконечным, но как только число становится меньше одного, он останавливается
        sum += num % 10
        #print(sum)
        num = num//10
        #print(num)
        #print()
        if num < 1:
            sum = int(sum)
            print(sum)
            break

    print("Again? Press 'N' to exit, press any other key to continue")
    want = input()
    if want == 'N' or want == 'n':
        do = 0