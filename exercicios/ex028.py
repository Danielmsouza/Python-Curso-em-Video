'''Guessing game. Try to guess which number from 0 to 5 the computer chose'''
'''Jogo de adivinhação. Tente descobrir que numero de 0 a 5 o computador escolheu'''

from random import randint
from time import sleep
computer = randint(0, 5)
print ('-=-' * 20)
print('I will think of a number between 0 and 5. Try to guess...')
print ('-=-' * 20)
player = int(input('What number did I think of? '))
print('Processing...')
sleep(1)
if player == computer:
    print('Congratulations you won')
else:
    print(f'Sorry! I thought in the number {computer} and you chose the number {player}')