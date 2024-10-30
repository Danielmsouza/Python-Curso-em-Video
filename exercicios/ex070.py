'''Program that reads the name and price of different products. Then ask if you want to continue and at the end it shows the total amount spent on the purchase; how many products cost more than $1,000; what is the name of the cheapest product'''
'''Programa que le o nome e o preço de varios produtos. Depois perguntar se quer continuar e no final mostra qual é o total gasto na compra; quantos produtos custam mais de $ 1000; qual é o nome do produto mais barato'''
totalspent = quantproduct = smaller = count = 0
cheap = ' '
while True:
    print('-' * 30)
    name = str(input('Name of product: ')).strip()
    price = float(input('Price of product: '))
    totalspent += price
    count += 1
    print('-' * 30)
    if price >= 1000:
        quantproduct += 1
    if count == 1:
        smaller = price
        cheap = name
    else:
        if price < smaller:
            smaller = price
            cheap = name
    cont = ' '
    while cont not in 'Y/N':
        cont = str(input('Do you want to continue?[Y/N] ')).strip().upper()[0]
    if cont == 'N':
        break
print('-' * 30)
print(f'The total spent on the purchase was $ {totalspent}.')
print(f'{quantproduct} products cost more than $1000')
print(f'The cheapest product was {cheap}')