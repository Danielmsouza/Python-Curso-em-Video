'''Program that reads the a person's sex but only accepts the values 'M' or 'F'.'''
'''Programa que le o sexo de uma pessoa mas so aceita os valores 'M' ou 'F'.'''

sex = str(input('Enter the sex: [M/F]: ')).strip().upper()[0]
while sex not in 'MF':
    sex = str(input('Error. Please enter the sex: ')).strip().upper()[0]
print(f'Sex {sex}, correct')
