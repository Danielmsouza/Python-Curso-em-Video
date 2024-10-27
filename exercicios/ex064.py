'''Program that reads several numbers. The program only stops when 999 is entered and shows the number of numbers entered and the sum between them'''
'''Programa que le varios numeros. O programa so vai parar quando digitado 999 e no final mostra a quantidade de numeros digitados e a soma entre eles'''

number = cont = sum = 0
number = int(input('Enter the number [999 to stop]: '))
while number != 999:
    sum += number
    cont += 1
    number = int(input('Enter the number [999 to stop]: '))
print(f'You typed {cont} numbers and the sum between them were {sum}')