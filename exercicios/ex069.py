'''Program that reads the age and sex of different people. For each registered person, the program will ask if the user wants to continue. In the end it shows
how many people are over 18, how many men are registered and how many women are under 20'''
'''Programa que le a idade e o sexo de varias pessoas. A cada pessoa cadastrada o programa ira perguntar se o usuario quer continuar. No final mostra
quantas pessoas tem mais de 18 anos, quantos homens cadastrados e quantas mulheres tem menos de 20 anos'''
tot18 = totM = totF = 0
while True:
    print('-' * 30)
    age = int(input('Age: '))
    sex = ' '
    while sex not in 'M/F':
        sex = str(input('sex: [M/F] ')).strip().upper()[0]
    print('-' * 30)
    if age >= 18:
        tot18 += 1
    if sex == 'M':
        totM += 1
    if sex == 'F' and age < 20:
        totF += 1
    cont = ' '
    while cont not in 'Y/N':
        cont = str(input('Do you want to continue?[Y/N] ')).strip().upper()[0]
    if cont == 'N':
        break
print(f'Total of the people with more 18 age: {tot18}')
print(f'in total we have {totM} men')
print(f'and have {totM} women over 20 years')
