'''Program that reads 3 numbers and shows the BIGGEST and SMALLEST values'''
'''Programa que le 3 numeros e mostra qual é o MAIOR e o MENOR valor'''

number1 = int(input('Enter the First value: '))
number2 = int(input('Enter the Second value: '))
number3 = int(input('Enter the Third value: '))
smallest = number1
if number2 < number1 and number2 < number3:
    smallest = number2
if number3 < number1 and number3 < number2:
    smallest = number3
biggest = number1
if number2 > number1 and number2 > number3:
    biggest = number2
if number3 > number1 and number3 > number2:
    biggest = number3

print(f'The Smallest value was {smallest}')
print(f'The Biggest value was {biggest}')
