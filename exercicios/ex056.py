'''Program that reads the name, age and sex of 4 people and shows. The average age, What is the name of the oldest man and how many women are under 20 years old'''
'''Programa que le o nome, idade e sexo de 4 pessoas e mostre: A media de idades, Qual é o nome do homem mais velho e quantas mulheres tem menos de 20 anos'''

sum_age = 0
average = 0
oldest_man = 0
name_old = ''
women = 0
for person in range(1, 5):
    print(f' -------{person}° Person -------')
    name = str(input('Name: ')).strip()
    age = int(input('Age: '))
    sex = str(input('Sex [M/F]: ')).strip()
    sum_age += age
    if person == 1 and sex in 'Mm':
        oldest_man = age
        name_old = name
    if sex in 'Mm' and age > oldest_man:
        oldest_man = age
        name_old = name
    if sex in 'Ff' and age < 20:
        women += 1
average = sum_age / 4
print(f'The average age is {average} years')
print(f'The oldest man have {oldest_man} years and the name is {name_old}')
print(f'There are {women} women over 20 years old')