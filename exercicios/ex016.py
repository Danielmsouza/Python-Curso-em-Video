'''Program that shows the entire portion of the number entered'''
'''Programa que mostra a porção inteira do numero digitado'''

from math import trunc
number = float(input('Enter the number: '))
print(f'The number entered was {number} and its integer part is {trunc(number)}')
