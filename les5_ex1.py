# На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга.
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет.
# Все конфеты оппонента достаются сделавшему последний ход.
# Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?
import random


marbles = 2021
moves = []


def move_comp():
    if marbles < 29:
        print(f'The computer took {marbles} marbles')
        return marbles
    elif marbles < 57:
        a = random.randint(1, 28)
        while marbles - a < 28:
            a = random.randint(1, 28)
        print(f'The computer took {a} marbles')
        return a
    else:
        a = random.randint(1, 28)
        print(f'The computer took {a} marbles')
        return a


def move_human():
    human_move = 0
    while human_move < 1 or human_move > 28:
        try:
            a = int(input('Your move. How many marbles do you take? '))
            if a < 1 or a > 28:
                print('Enter only numbers from 1 to 28!')
            else:
                print(f'You took {a} marbles')
                return a
        except:
            print('Enter only numbers from 1 to 28!')


def check_win(marble):
    if marble == 0:
        return True


def game(first):
    global marbles
    while True:
        if first == 0:
            marbles = marbles - move_human()
            print(f'There are {marbles} marbles left')
            if check_win(marbles):
                print('Human WINS!')
                break
            marbles = marbles - move_comp()
            print(f'There are {marbles} marbles left')
            if check_win(marbles):
                print('Computer WINS!')
                break
        else:
            marbles = marbles - move_comp()
            print(f'There are {marbles} marbles left')
            if check_win(marbles):
                print('Computer WINS!')
                break
            marbles = marbles - move_human()
            print(f'There are {marbles} marbles left')
            if check_win(marbles):
                print('Human WINS!')
                break


print(
    'Welcome to the game! Here are the rules:\n'
    'Two players: a human VS a computer.\n'
    f'There are {marbles} marbles. You can take any amount from 1 to 28.\n'
    'The player who takes the last marbles wins.\n'
    'First player is chosen randomly.\n'
    'Let\'s begin!'
    )
f_move = random.randint(0, 1)
if f_move == 0:
    print('Human moves first')
else:
    print('Computer moves first')

game(f_move)