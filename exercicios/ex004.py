'''Programa que lê algo pelo teclado e mostra o seu tipo primitivo e informações sobre ele'''

algo = input('Digite algo: ')
print('O tipo primitivo desse valor é ',type(algo))
print('So tem espaços? ', algo.isspace())
print('So tem numeros? ', algo.isnumeric())
print('É alfabetico? ', algo.isalpha())
print('É alfanumerico? ',algo.isalnum())
print('Esta em maiusculas? ', algo.isupper())
print('Esta em minusculas? ', algo.islower())
print('Esta capitalizada? ', algo.istitle())
