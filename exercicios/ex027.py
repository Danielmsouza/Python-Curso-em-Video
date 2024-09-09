'''Program that reads the full name and show in seconds the first and the last name separately'''
'''Programa que le o nome completo e mostra em segundos o primeiro e o ultimo nome separadamente'''

n = str(input('Enter the full name: ')).strip()
name = n.split()
print(f'Your first name is {name[0]}')
print(f'Your last name is {name[len(name)-1]}')
