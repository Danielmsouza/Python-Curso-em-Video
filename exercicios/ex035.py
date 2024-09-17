'''Program that reads the lenght of 3 straight lines and tells whether or not they can form a triangle'''
'''Programa que le o comprimento de 3 retas e diga se podem ou não formar um triangulo'''

print('-=' * 20)
print('triangle analysis')
print('-=' * 20)
line1 = float(input('Enter the first line: '))
line2 = float(input('Enter the second line: '))
line3 = float(input('Enter the third line: '))
if line1 < line2 + line3 and line2 < line1 + line3 and line3 < line1 + line2:
    print('The lines can form a triangle')
else:
    print("The lines can't form a triangle")