'''Program that reads the length of opposite and adjacent legs and shows the length of the hypotenuse'''
'''Programa que le o comprimento do cateto oposto e do cateto adjacente e mostra o comprimento da hipotenusa'''

from math import hypot
co = float(input('Enter the CO: '))
ca = float(input('Enter the CA: '))
hi = hypot(co, ca)
print(f'The hypotenuse is {hi}')
