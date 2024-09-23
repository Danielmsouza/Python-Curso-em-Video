'''Program that reads the year of birth and shows the category according to age: 
Up to 9 years old: MIRIM    Up to 14 years old: CHILDREN    Up to 19 years old: JUNIOR       Up to 25 years old: Senior      Above: MASTER'''
'''Programa que le o ano de nascimento e mostre a categoria de acordo com a idade: 
Até 9 anos: MIRIM   Até 14 anos: INFANTIL   Até 19 anos: JUNIOR     Até 25 anos: Senior     Acima: MASTER'''

from datetime import date
today = date.today().year
birth = int(input('Enter the year of birth: '))
age = today - birth
print(f'The athlete has {age} years')
if age <= 9:
    print('Classification: MIRIM')
elif age <= 14:
    print('Classification: CHILDREN')
elif age <= 19:
    print('Classification: JUNIOR')
elif age <= 25:
    print('Classification: SENIOR')
elif age > 25:
    print('Classification: MASTER')