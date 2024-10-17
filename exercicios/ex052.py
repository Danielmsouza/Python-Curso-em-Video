'''Program that reads an integer and shows whether the number is prime or not'''
'''Programa que le um numero inteiro e diga se le é ou não um numero primo'''

number = int(input('Enter the number: '))
tot = 0
for c in range(1, number + 1):
    if number % c == 0:
        print('\033[33m', end='')
        tot +=1
    else:
        print('\033[31m', end='')
    print(f'{c}', end='')
print(f'\n\033[mO number {number} was divided {tot} times')
if tot == 2:
    print('The numner is prime')
else:
    print("The number isn't prime")