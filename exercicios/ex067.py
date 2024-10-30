'''Program that shows the multiplication table of several numbers, one at a time, for each value entered by the user. The program will stop when the requested number is negative'''
'''Programa que mostre a tabuada de varios numeros um de cada vez para cada valor digitado pelo usuario. O programa sera interrompido quando o numero solicitado for negativo'''

while True :
    number = int(input('Do you want to see the multiplication table of which value? '))
    if number < 0:
        break
    print('-' * 30)
    for c in range (1, 11):
        print(f'{number} x {c} = {number * c}')
    print('-' * 30)