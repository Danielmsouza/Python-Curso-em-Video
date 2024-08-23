'''Program that calculate the price to pay for renting a car ( $60 per day and $0.15 per Km)'''
'''Programa que calcula o preço a pagar pelo aluguel de um carro ($60 por dia e $0.15 por Km)'''

days = int(input('How many days was the car used? '))
Km = float(input('How many Km were convered? '))
price = (days * 60) + (Km * 0.15)

print(f'The total price to be paid for the car is ${price}')