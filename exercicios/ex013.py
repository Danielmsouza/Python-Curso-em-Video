'''Program that calculate the new salary'''
'''Programa que calcula o novo salario'''

salary = float(input('What is the salary ? '))
increase = float(input('What is the percentage inscrease in salary ? '))
new_salary = salary + (salary * increase / 100)

print(f'The salary is ${salary}, with the increase of the {increase}%, the new salary is ${new_salary}')