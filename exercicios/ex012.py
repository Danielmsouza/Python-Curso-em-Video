'''Program that calculates discount'''
'''Programa que calcula descontos'''

price = float(input('What is the value of product? '))
discount = float(input('What is the value of discount? '))
new_price = price - (price * discount / 100)

print(f'The price of the product with discount is {new_price}')
