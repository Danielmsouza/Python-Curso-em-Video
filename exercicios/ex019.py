'''Program that reads 4 names and choice one name'''
'''Programa que le 4 nomes e sorteia um nome'''

from random import choice
name1 = str(input('Enter the first name: '))
name2 = str(input('Enter the second name: '))
name3 = str(input('Enter the third name: '))
name4 = str(input('Enter the fourth name: '))
lista = [name1, name2, name3, name4]
chosen = choice(lista)
print(f'The name chosen was {chosen}')
