'''Program that reads speed. If you exceed 80Km/h, show a message informing you that you have been fined. The fine will cost $7 por each kilometer over the limit'''
'''Programa que le a velocidade. Se ultrapassar 80Km/h, mostre uma mensagem dizendo que foi multado. A multa vai custar $7 por cada Km acima do limite'''

speed = float(input('Enter the speed: '))
if speed > 80:
    print(f'Over the limit! ')
    fine = (speed - 80) * 7
    print(f'Your fine will be ${fine}')
print('Drive safely')