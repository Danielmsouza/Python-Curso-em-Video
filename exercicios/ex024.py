'''Program that reads the name of a city and shows whether or not it begins with the name SANTO'''
'''Programa que le o nome de uma cidade e mostra se ela começa ou não com o nome SANTO'''

city = str(input('Enter the name: ')).strip()
print(city[:5].upper() == 'SANTO')
