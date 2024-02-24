'''Program that reads something from the keyboard and shows its primitive type and information about it'''
'''Programa que lê algo pelo teclado e mostra o seu tipo primitivo e informações sobre ele'''

something = input('Type something: ')
print('The primitive type of this value is ',type(something))
print('Do you have only spaces ? ', something.isspace())
print('Do you have only numbers ? ', something.isnumeric())
print('Is it alphabetical ? ', something.isalpha())
print('Is it alphanumeric ? ',something.isalnum())
print('Is it in capital letters ? ', something.isupper())
print('Is it in lower case ? ', something.islower())
print('Is it capitalized ? ', something.istitle())
