'''Prgram that reads 4 names and show the order drawn'''
'''Programa que le 4 nomes e mostre a ordem sorteada'''

import random
name1 = str(input('Enter the first name: '))
name2 = str(input('Enter the second name: '))
name3 = str(input('Enter the third name: '))
name4 = str(input('Enter the fourth name: '))
lista = [name1, name2, name3, name4]
random.shuffle(lista)
print(f'The order drawn was {lista}')