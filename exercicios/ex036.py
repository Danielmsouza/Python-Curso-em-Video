'''Program that analyzes the possibility of a loan to purchase a house. If the monthly payment exceeds 30 % of the salary, the loan will be denied'''
'''Programa que analisa a possibilidade de um emprestimo para compra de uma casa.Se a prestação mensal exceder 30% do salario o emprestimo sera negado'''

house = float(input('How much does the house cost? $ '))
salary = float(input('What is your salary? $ '))
years = int(input('How long is the financing? '))
installments = house / (years * 12)
minimum = salary * 30 / 100
print(f'To pay a ${house} house in {years} years')
print(f'The installments will be ${installments}')
if installments <= minimum:
    print('Loan granted')
else:
    print('Load denied')