'''Program that reads a number and displays its factorial'''
'''Programa que le um numero e mostre seu fatorial'''

number = int(input('Enter the number: '))
c = number
factorial = 1
print(f'calculating {number}! = ', end='')
while c > 0:
    print(f'{c}', end='')
    print(f' x ' if c > 1 else ' = ', end='')
    factorial *= c
    c -= 1
print(f'{factorial}')