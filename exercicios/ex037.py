'''Program that converts an integer to binary, octal or hexadecimal'''
'''Programa que converte um numero inteiro em binario, octal ou hexadecimal'''

number = int(input('Enter the number: '))
print('''Choose the option to convert:
[1] convert to Binary
[2] convert to Octal
[3] convert to Hexadecimal''')
option = int(input('Your option: '))
if option == 1:
    print(f'{number} converted to Binary is {bin(number)[2:]}')
elif option == 2:
    print(f'{number} converted to Octal is {oct(number)[2:]}')
elif option == 3:
    print(f'{number} converted to Hexadecimal is {hex(number)[2:]}')
else:
    print('Invalid option, try again.')