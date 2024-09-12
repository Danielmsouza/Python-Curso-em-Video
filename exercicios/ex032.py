'''Program that reads a year and show if it is LEAP YEAR'''
'''Programa que le um ano e mostra se ele é BISSEXTO'''

from datetime import date
year = int(input('Enter the year, input 0 for atual year: '))
if year == 0:
    year = date.today().year
if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    print(f'The year {year} is LEAP YEAR')
else:
    print(f'The year {year} is not LEAP YEAR')