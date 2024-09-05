'''Programa que le um numero entre 0 e 9999 e mostra cada um dos digitos separados'''
'''Program that reads a number between 0 and 9999 and displays each digit separately'''

number = int(input('Enter the number: '))
u = number // 1 % 10
d = number // 10 % 10
c = number // 100 % 10
m = number // 1000 % 10
print(f'Unit: {u}')
print(f'Dozens {d}')
print(f'Hundred: {c}')
print(f'Thousand: {m}')