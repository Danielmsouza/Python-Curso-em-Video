'''Program that calculates the sum of all odd numbers that are multiples of 3 and range from 1 to 500'''
'''Programa que calcula a soma entre todos os numeros impares que são multiplos de 3 e que encontram no intervalo de 1 até 500'''

sum = 0
cont = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        cont = cont + 1
        sum = sum + c
print(f' The sum of all numbers are {sum}')