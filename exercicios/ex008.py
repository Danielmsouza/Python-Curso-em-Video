'''Program that reads a value in meters and displays it converted into centimeters and millimeter'''
'''Programa que le um valor em metros e o exibe convertido em centimetros e milimetros'''

meter = float(input('Enter the distance in meters: '))
centimeters = meter * 100
millimeters = meter * 1000

print(f'The distance in meters of {meter}m matches to {centimeters}cm or {millimeters}mm')
