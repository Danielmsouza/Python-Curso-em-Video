'''Program that takes several numbers. The program only stops when 999 is entered and at the end it shows how many numbers were entered and the sum between them'''
'''Programa que le varios numeros. O programa so para quando for digitado 999 e no final, mostre quantos numeros fora digitados e qual a soma entre eles'''

sum = cont = 0
while True :
    number = int(input('Enter the number:[999 to stop] '))
    if number == 999:
        break
    cont += 1
    sum += number
print(f'The sum of the {cont} values were {sum}! ')