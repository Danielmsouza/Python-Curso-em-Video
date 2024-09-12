'''Program thah calculates the ticket price. Charging $0.50 per Km for trips of up to 200Km and $0.45 for longer trips'''
'''Programa que calcula o preço da passagem. Cobrando $0.50 por Km para viagens de até 200Km e $0.45 para viagens mais longas'''

distance = float(input('Enter the distance: '))
if distance <= 200:
    price = distance * 0.50
else:
    price = distance * 0.45
print(f'The price of your ticket will cost ${price}')