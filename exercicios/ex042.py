'''Adding resources in exercise 35'''
'''Acrescentando recursos no exercicio 35'''

print('-=' * 20)
print('triangle analysis')
print('-=' * 20)
line1 = float(input('Enter the first line: '))
line2 = float(input('Enter the second line: '))
line3 = float(input('Enter the third line: '))
if line1 < line2 + line3 and line2 < line1 + line3 and line3 < line1 + line2:
    print('The lines can form a triangle')
    if line1 == line2 == line3:
        print('EQUILATERO!')
    elif line1 != line2 != line3 != line1:
        print('ESCALENO!')
    else:
        print('ISOSCELES')
else:
    print("The lines can't form a triangle")