'''Improve the exercise 028'''
'''Melhore o exercicio 028'''

from random import randint
from time import sleep
computer = randint(0, 10)
print ('-=-' * 20)
print('I will think of a number between 0 and 10. Try to guess...')
print ('-=-' * 20)
correct = False
attempts = 0
while not correct:
    player = int(input('What number did I think of? '))
    print('Processing...')
    sleep(0.2)
    attempts += 1
    if player == computer:
        correct = True
    else:
        if player < computer:
            print('You entered a lower number, please try again')
        elif player > computer:
            print('You entered a larger number, please try again')
print(f'You Win with {attempts} attempts')