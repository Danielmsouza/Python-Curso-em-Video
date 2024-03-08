'''Program that reads a value in meters and displays it converted into centimeters and millimeters'''
'''Programa que le um valor em metros e o exibe convertido em centimetros e milimetros'''

measure = float(input('Enter the distance in meters: '))
cm = measure * 100
mm = measure * 1000
print(f'The measure of {measure}m  matches to {cm}cm and {mm}mm')