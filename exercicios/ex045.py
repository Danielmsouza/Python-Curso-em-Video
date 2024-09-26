'''JOKENPO Game'''
'''jogo Pedra, papel, tesoura'''

from random import randint
from time import sleep
items = ('Pedra', 'Papel', 'Tesoura')
pc = randint(0, 2)
print('''Your options: 
      [ 0 ] PEDRA
      [ 1 ] PAPEL
      [ 2 ] TESOURA ''')
gamer = int(input('What is your move? '))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO')
sleep(1)
print('-=' * 11)
print(f'Pc Played {items[pc]}')
print(f'Gamer Played {items[gamer]}')

if pc == 0:
    if gamer == 0:
        print('DRAW')
    elif gamer == 1:
        print('Gamer won')
    elif gamer == 2:
        print('Pc won')
    else:
        print('Error! ')
if pc == 1:
    if gamer == 1:
        print('DRAW')
    elif gamer == 2:
        print('Gamer won')
    elif gamer == 0:
        print('Pc won')
    else:
        print('Error! ')
if pc == 2:
    if gamer == 2:
        print('DRAW')
    elif gamer == 0:
        print('Gamer won')
    elif gamer == 1:
        print('Pc won')
    else:
        print('Error! ')
