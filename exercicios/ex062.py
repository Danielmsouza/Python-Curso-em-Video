'''Program that reads the first term and the ratio of AP, then shows the first 10 terms of this progression. Version 3.0 '''
'''Programa que le o primeiro termo e a razão de uma PA, depois mostre os 10 primeiros termos dessa progressão. Versão 3.0'''

first = int(input('First term: '))
ratio = int(input('Enter the ratio: '))
term = first
cont = 1
total = 0
plus = 10
while plus != 0:
    total = total + plus
    while cont <= total:
        print(f'{term} ', end='> ')
        term += ratio
        cont += 1
    print('PAUSE')
    plus = int(input('How many more terms do you want to show? '))
print(f'Program completed with {total} terms displayed')
