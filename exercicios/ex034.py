'''Program that reads your salary and calculates the amount of your increase. For salaries above $1250 there will be a 10% increase and for salaries below the increase will be 15%'''
'''Programa que le o salario e calcula o valor do seu aumento. Para salarios superiores a $1250 tem um aumento de 10% e para salarios inferiores o aumento vai ser de 15%'''

salary = float(input('what is your salary? '))
if salary <= 1250:
    new_salary = salary + (salary * 15 / 100)
else:
    new_salary = salary + (salary * 10 / 100)
print(f'How won ${salary} you will earn ${new_salary} now.')