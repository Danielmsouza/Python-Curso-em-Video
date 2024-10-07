'''Program that reads the first term and the ratio of AP, then shows the first 10 terms of this progression '''
'''Programa que le o primeiro termo e a razão de uma PA, depois mostre os 10 primeiros termos dessa progressão'''

first = int(input('First term: '))
ratio = int(input('Enter the ratio: '))
ten = first + (10 - 1) * ratio
for c in range(first, ten + ratio, ratio):
    print(f'{c} ', end='> ')
print('FIM')