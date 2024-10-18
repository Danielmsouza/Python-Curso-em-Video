'''Program that reads the year of birth of 7 people and shows how many people are not yet 18 years old.'''
'''Programa que le o ano de nascimento de 7 pessoas e mostre quantas pessoas ainda não possuem 18 anos.'''
from datetime import date
today = date.today().year
bigger = 0
smaller = 0
for person in range(1,8):
    birth = int(input(f'What year was the {person} born: '))
    age = today - birth
    if age >= 18:
        bigger += 1
    else:
        smaller += 1
print(f'There are {bigger} people over 18 years old')
print(f'There are {smaller} people under 18 years old')