'''Program that calculates the price to be paid for the product considering the normal price and payment conditions:
Cash/cheque payment: 10% discount                   Card payment: 5% discount
up to 2x on card: normal price                      3x or more on card: 20% interest'''
'''Programa que calcula o preço a ser pago pelo produto considerando o preço normal e condição de pagamento:
A vista no dinheiro/cheque: 10% de desconto          a vista no cartão: 5% de desconto
em ate 2x no cartão: preço normal                    3x ou mais no cartão: 20% de juros'''

price = float(input('Enter the shopping prices:'))
print('''PAYMENT METHODS
[1] Cash/cheque
[2] Card
[3] 2x on card
[4] 3x or more on card''')
option = int(input('What is the option? '))
if option == 1:
    total = price - (price * 10 / 100)
elif option == 2:
    total = price - (price * 5 / 100)
elif option == 3:
    total = price
    installments = total / 2
    print(f'Each installment will be ${installments}')
elif option == 4:
    total = price + (price * 20 / 100)
    totpar = int(input('How many installments?'))
    installments = total / totpar
    print(f'Each installment will be ${installments}')
else:
    total = 0
    print('Error')
print(f'Total purchase ${total}')