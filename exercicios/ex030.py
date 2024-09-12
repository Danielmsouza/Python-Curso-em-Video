'''Program that reads an integer and show whether it is PAIR or ODD'''
'''Programa que le um numero inteiro e mostra se ele é PAR ou IMPAR'''

number = int(input('Enter the number: '))
result = number % 2
if result == 0:
    print(f'The number {number} is PAIR')
else:
    print(f'The number {number} is ODD')