'''Program that reads the first term and the ratio of AP, then shows the first 10 terms of this progression. Version 2.0 '''
'''Programa que le o primeiro termo e a razão de uma PA, depois mostre os 10 primeiros termos dessa progressão. Versão 2.0'''

first = int(input('First term: '))
ratio = int(input('Enter the ratio: '))
term = first
cont = 1
while cont <= 10:
    print(f'{term} ', end='> ')
    term += ratio
    cont += 1
print('FIM')