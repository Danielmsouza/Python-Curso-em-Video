'''Program that reads an angle and shows the value of sine, cosine and tangent on the screen'''
'''Programa que le um angulo e mostre na tela o valor do seno, cosseno e tangente'''

from math import radians,sin,cos,tan
angle = float(input('Enter the angle: '))
sine = sin(radians(angle))
print(f'The angle of {angle} have the sine of {sine}')
cosine = cos(radians(angle))
print(f'The angle of {angle} have the cosine of {cosine}')
tangent = tan(radians(angle))
print(f'The angle of {angle} have the tangent of {tangent}')
