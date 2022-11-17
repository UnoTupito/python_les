# Tic-Tac-Toe
import random


def who_wins(chip):
    if chip == CHIP_COMP:
        print('Computer wins!')
    else:
        print('You win!')


def check_win():
    for i in range(len(field)):
        if field[i][0] != EMPTY_PLACE and field[i][0] == field[i][1] == field[i][2]:
            who_wins(field[i][0])
            return True
        elif field[0][i] != EMPTY_PLACE and field[0][i] == field[1][i] == field[2][i]:
            who_wins(field[0][i])
            return True
    if field[1][1] != EMPTY_PLACE and (field[0][0] == field[1][1] == field[2][2] or field[0][2] == field[1][1] == field[2][0]):
        who_wins(field[1][1])
        return True
    return False


def valid_move(num):
    if num.isdigit() and 0 < int(num) < 4:
        return True
    else:
        print('You need to enter a number from 1 to 3')
        return False


def move_human():
    global field
    print('Your move')
    chip_put = False
    while not chip_put:
        num_got = False
        while not num_got:
            row = input('Enter the row: ')
            num_got = valid_move(row)
            if num_got:
                row = int(row)
        num_got = False
        while not num_got:
            col = input('Enter the column: ')
            num_got = valid_move(col)
            if num_got:
                col = int(col)
        if field[row-1][col-1] == EMPTY_PLACE:
            field[row-1][col-1] = CHIP_HUMAN
            chip_put = True
        else:
            print('This place is not empty')
    print_field()


def move_comp():
    global field
    print('Computer moves:')
    num_got = False
    while not num_got:
        row = random.randint(0, 2)
        col = random.randint(0, 2)
        if field[row][col] == EMPTY_PLACE:
            field[row][col] = CHIP_COMP
            num_got = True
    print_field()


def make_field():
    global field
    for i in range(3):
        field.append([])
        for j in range(3):
            field[i].append(EMPTY_PLACE)


def print_field():
    global field
    for i in range(len(field)):
        for j in range(len(field)):
            print(field[i][j], end='')
            if j < len(field)-1:
                print('|', end='')
        print()


CHIP_HUMAN = 'X'
CHIP_COMP = 'O'
EMPTY_PLACE = '*'
print('Let\'s play tick-tack-toe!')
field = []
make_field()
print_field()
move = 1
win = False
while move <= 9:
    if move % 2 != 0:
        move_human()
    else:
        move_comp()
    win = check_win()
    if win:
        break
    move += 1
    if move == 10:
        print('No one wins')


