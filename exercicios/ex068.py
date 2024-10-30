'''Program that works odd or even with the computer. The game will only stop when the player loses, showing the total number of wins'''
'''Programa que joga par ou impar com o computador. O jogo so sera interrompido quando o jogador perder, mostrando o total de vitorias'''

from random import randint
v = 0
while True:
    player = int(input('Enter the value: '))
    computer = randint(0, 10)
    total = player + computer
    type = ' '
    while type not in 'PO':
        type = str(input('pair or odd? [P/O] ')).strip().upper() [0]
    print(f'You played {player} and the computer {computer}. Total of the {total}')
    if type == 'P':
        if total % 2 == 0:
            print('You win')
            v += 1
        else:
            print('You lost')
            break
    elif type == 'O':
        if total % 2 == 1:
            print('You win')
            v += 1
        else:
            print('You lost')
            break
    print('Shall we play again? ')
print(f'Game Over! You win {v} times')