'''Program that reads 2 integers and displays a message saying which number is the bigger or whether they are equal '''
'''Programa que le 2 numeros inteiros e mostre uma mensagem dizendo qual numero é maior ou se são iguais'''

number1 = int(input('Enter the first number: '))
number2 = int(input('Enter the second number: '))
if number1 > number2 :
    print('The first number is bigger')
elif number2 > number1:
    print('The second number is bigger')
else:
    print('The numbers are equal')