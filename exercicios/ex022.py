'''Programa que lê o nome completo de uma pessoa e mostre: nome da pessoa em maiusculas, minusculas, total de letras e quantidade de letras do primeiro nome'''
'''Program that reads a person's full name and displays: the person's name in uppercase, lowercase, total letters and number of letters in the first name'''

name = str(input('Enter the full name: ')).strip()
print(f'Your name in uppercase is {name.upper()}')
print(f'Your name in lowercase is {name.lower()}')
print(f'Your name has {len(name) - name.count(" ")} letters')
print(f'Your first name has {name.find(" ")} letters')
