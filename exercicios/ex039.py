'''Program that reads the year of birth of a young person and informs if he is still going to enlist in the army, if he needs to enlist or if he is late'''
'''Programa que le o ano de nascimento de um jovem e informa se ele ainda vai se alistar ao serviço militar, se ele precisa se alistar ou se ja passou do tempo'''

from datetime import date
actual = date.today().year
birth = int(input('Enter the year of birth: '))
age = actual - birth
print(f'Who was born in {birth} is {age} years em {actual}')
if age == 18:
    print('You need to enlist')
elif age < 18:
    balance = 18 - age
    print(f'There are still {balance} years left to enlist')
elif age > 18:
    balance = age - 18
    print(f'you should have enlisted {balance} years ago')